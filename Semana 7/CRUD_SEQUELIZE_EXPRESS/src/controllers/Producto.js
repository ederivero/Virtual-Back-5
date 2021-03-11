const { Producto } = require("../config/Creacion");

const crearProducto = async (req, res) => {
  const nuevoProducto = await Producto.create(req.body).catch((error) =>
    res.status(500).json({
      success: false,
      content: error,
      message: "Error al crear el producto",
    })
  );
  return res.status(201).json({
    success: true,
    content: nuevoProducto,
    message: "Producto creado exitosamente",
  });
};

module.exports = {
  crearProducto,
};
