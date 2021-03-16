const { conexion } = require("../config/Sequelize");
const {
  Producto,
  Promocion,
  Detalle,
  CabeceraNota,
} = require("../config/Relaciones");

const crearVenta = async (req, res) => {
  const { productos } = req.body;
  // primero defino la transaccion
  const transaccion = await conexion.transaction();
  // creamos nuestra cabecera de la venta
  const cabeceraVenta = await CabeceraNota.create(
    {
      cabeceraSerie: "BBB1",
      cabeceraTotal: 0.0,
      cabeceraDescuento: 0.0,
      cabeceraSubTotal: 0.0,
    },
    { transaction: transaccion }
  );
  let descuentoTotal = 0;

  // 1. ver si el producto tiene promocion vigente
  productos.forEach(async (producto) => {
    const { id, cantidad } = producto;
    const productoEncontrado = await Producto.findByPk(id, {
      include: {
        // dentro del modelo promocion solamente quiero la primera coincidencia de la promocion mediante el ordenamiento de la columna promocionFechaHasta de manera descendente
        model: Promocion,
        order: [["promocionFechaHasta", "DESC"]],
        limit: 1,
      },
    });
    // ahora iteramos todas las posibles promociones del producto (las vigentes y no vigentes)
    const { promociones } = productoEncontrado;
    console.log("Producto encontrado");
    console.log(productoEncontrado.toJSON());
    const fechaActual = new Date();
    let promocionActiva;
    promociones.forEach((promocion) => {
      if (fechaActual < promocion.promocionFechaHasta) {
        console.log("sige vigente la promo!!");
        promocionActiva = promocion;
        // aca lo haria
        const descuentoTemporal = promocion.promocionDescuento * cantidad;
        const precioNormal = productoEncontrado.productoPrecio * cantidad;
        descuentoTotal += precioNormal - descuentoTemporal;
        // descuentoTotal = descuentoTotal + (precioNormal - descuentoTemporal)
      }
      console.log(promocion.toJSON());
    });
    console.log("La promocion activa es:");
    console.log(promocionActiva);
    // aqui creamos el detalle de la venta
    const detalleVenta = await Detalle.create({
      detalleCantidad: cantidad,
      detallePrecioUnitario: promocionActiva
        ? promocionActiva.promocionDescuento
        : productoEncontrado.productoPrecio,
      prod_id: id,
      cab_id: cabeceraVenta.cabeceraId,
    });
    // ahora actualizo las cantidades de mi producto
    await Producto.update(
      {
        productoCantidad: productoEncontrado.productoCantidad - cantidad,
      },
      {
        where: {
          productoId: id,
        },
        transaction: transaccion,
      }
    );

    // TAREA!!!: indicar si es que tiene promocion activa dar ese precio, caso contrario dar el precio original del producto
  });

  // 2. crear el detalle de la venta
  // 3. restar la cantidad del producto del inventario
  // 4. Agregar el total a la cabecera de la venta
  // 5. Generar la cabecera
  // NOTA: se recomienda solamente usar la transaccion en sentencias que modifique nuestra bd (insert, delete, update)
  return res.send("ok");
};

module.exports = {
  crearVenta,
};
