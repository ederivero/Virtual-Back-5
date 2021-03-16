const { conexion } = require("../config/Sequelize");
const { Producto, Promocion } = require("../config/Relaciones");

const crearVenta = async (req, res) => {
  const { productos } = req.body;
  // primero defino la transaccion
  const transaccion = await conexion.transaction();
  // 1. ver si el producto tiene promocion vigente
  productos.forEach(async (producto) => {
    const { id } = producto;
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
      }
      console.log(promocion.toJSON());
    });
    console.log("La promocion activa es:");
    console.log(promocionActiva);
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
