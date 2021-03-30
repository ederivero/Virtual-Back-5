import requests
from datetime import datetime
from .models import CabeceraComandaModel, ComprobanteModel, DetalleComandaModel


def emitirComprobante(pedido, cabecera_id):
    # sunat_transaction => sirve para indicar que tipo de transaccion estas realizando, generalmente se usara el valor de 1 "VENTA INTERNA"
    cliente_denominacion = ""
    # 6 => RUC, 1 => DNI , - => varios
    documento = 0  # el numero de documento que toca crear

    cliente_documento = pedido['cliente_documento']
    cliente_tipo_documento = pedido['cliente_tipo_documento']
    tipo_comprobante = pedido['tipo_comprobante']
    # buscamos ese pedido para jalar sus datos
    comanda = CabeceraComandaModel.objects.get(cabeceraId=cabecera_id)
    print(pedido)
    # sacamos el total del pedido
    total = float(comanda.cabeceraTotal)
    # el valor total sin el IGV
    total_gravada = total / 1.18
    # el valor total del IGV de la compra
    total_igv = total - total_gravada

    if len(pedido['cliente_documento']) > 0:
        # significa que el pedido fue mayor a 700 soles O el cliente dio su dni para la compra
        # ahora se busca la persona o entidad para extraer sus datos
        base_url_apiperu = "https://apiperu.dev/api/"
        if cliente_tipo_documento == "RUC":
            base_url_apiperu = base_url_apiperu + \
                "ruc/{}".format(cliente_documento)
        elif cliente_tipo_documento == "DNI":
            base_url_apiperu = base_url_apiperu + \
                "dni/{}".format(cliente_documento)

        headers = {
            "Authorization": "Bearer 6287da8da77342f7e4aab59b670dbe153f0e803c2553e7a7dcbcc7d2510ba793",
            "Content-Type": "application/json"
        }
        respuestaApiPeru = requests.get(url=base_url_apiperu, headers=headers)

        if cliente_tipo_documento == "RUC":
            documento = 6
            cliente_denominacion = respuestaApiPeru.json()[
                'data']['nombre_o_razon_social']
        elif cliente_tipo_documento == "DNI":
            documento = 1
            cliente_denominacion = respuestaApiPeru.json()[
                'data']['nombre_completo']
    else:
        if total > 700:
            return {
                'error': 'Para un monto mayor a 700 es necesario una identificacion'
            }
        # si el monto es menor a 700 soles entonces usaremos una identificacion generica para no buscar la identificacion del cliente
        documento = "-"
        cliente_denominacion = "VARIOS"
        cliente_documento = "VARIOS"
    # ahora rellenamos el detalle del comprobante
    # codigo => codigo interno que manejamos nosotros
    # unidad_de_medida => NIU = PRODUCTOS | ZZ = SERVICIOS

    items = []
    # me retorna todo el detalle de un pedido
    for detalle in comanda.cabeceraDetalles.all():
        precio_unitario = float(detalle.plato.platoPrecio)
        valor_unitario = precio_unitario / 1.18  # el precio unitario SIN IGV
        cantidad = detalle.detalleCantidad
        item = {
            "unidad_de_medida": "NIU",
            "codigo": detalle.plato.platoId,
            "descripcion": detalle.plato.platoDescripcion,
            "cantidad": cantidad,
            "valor_unitario": valor_unitario,
            "precio_unitario": precio_unitario,
            "subtotal": valor_unitario*cantidad,
            "tipo_de_igv": 1,
            "igv": (valor_unitario * cantidad) * 0.18,
            "total": precio_unitario * cantidad,
            "anticipo_regularizacion": False
        }
        items.append(item)
    # indicar la serie y numero de comprobante
    # Las facturas y notas asociadas con ellas empiezan con F
    # Las boletas y notas asociadas con ellas empiezan con B
    serie = ""
    ultimoComprobante = None
    numero = None
    if tipo_comprobante == "BOLETA":
        serie = "B001"
        # traer el ultimo comprobante que es boleta
        ultimoComprobante = ComprobanteModel.objects.filter(
            comprobanteTipo=1).order_by('-comprobanteNumero').first()
    elif tipo_comprobante == "FACTURA":
        serie = "F001"
        # traer el ultimo comprobante que es factura
        ultimoComprobante = ComprobanteModel.objects.filter(
            comprobanteTipo=2).order_by('-comprobanteNumero').first()
    if ultimoComprobante is None:
        numero = 1
    elif ultimoComprobante is not None:
        numero = ultimoComprobante.comprobanteNumero + 1

    cliente_email = pedido['cliente_email']
    observaciones = pedido['observaciones']
    comprobante_body = {
        "operacion": "generar_comprobante",
        "tipo_de_comprobante": tipo_comprobante,
        "serie": serie,
        "numero": numero,
        "sunat_transaction": 1,
        "cliente_tipo_de_documento": documento,
        "cliente_numero_de_documento": cliente_documento,
        "cliente_denominacion": cliente_denominacion,
        "cliente_direccion": "",
        "cliente_email": cliente_email,
        "fecha_de_emision": datetime.now().strftime("%d-%m-Y"),
        "moneda": 1,
        "porcentaje_de_igv": 18.00,
        "total_gravada": total_gravada,
        "total_igv": total_igv,
        "total": total,
        "detraccion": False,
        "observaciones": observaciones,
        "enviar_automaticamente_a_la_sunat": True,
        "enviar_automaticamente_al_cliente": True,
        "medio_de_pago": "EFECTIVO",
        "formato_de_pdf": "TICKET",  # A4, A5, TICKET
        "items": items
    }
    url_nubefact = "https://api.nubefact.com/api/v1/db267c95-40d8-4757-9731-588481167020"
    headers_nubefact = {
        "Authorization": "3b643f32df9d40f089ff1685774d41206f8b633d814646969d29da362afa527b",
        "Content-Type": "application/json"
    }
    respuestaNubefact = requests.post(
        url=url_nubefact, json=comprobante_body, headers=headers_nubefact)
    return respuestaNubefact.json()
