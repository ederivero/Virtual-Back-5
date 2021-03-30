import requests
from datetime import datetime
from .models import CabeceraComandaModel, DetalleComandaModel


def emitirComprobante(pedido, cabecera_id):
    # sunat_transaction => sirve para indicar que tipo de transaccion estas realizando, generalmente se usara el valor de 1 "VENTA INTERNA"
    cliente_denominacion = ""
    # 6 => RUC, 1 => DNI , - => varios
    documento = 0  # el numero de documento que toca crear

    cliente_documento = pedido['cliente_documento']
    cliente_tipo_documento = pedido['cliente_tipo_documento']
    # buscamos ese pedido para jalar sus datos
    pedido = CabeceraComandaModel.objects.get(cabeceraId=cabecera_id).first()
    # sacamos el total del pedido
    total = float(pedido['cabecera_total'])
    # el valor total sin el IGV
    total_gravada = total / 1.18
    # el valor total del IGV de la compra
    total_igv = total - total_gravada

    if len(pedido['cliente_documento'] > 0):
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
