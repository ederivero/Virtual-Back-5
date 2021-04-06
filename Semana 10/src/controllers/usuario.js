const { Usuario } = require("../config/mongoose");

const registro = async (req, res) => {
  const objUsuario = new Usuario(req.body);
  objUsuario.encriptarPassword(req.body.password);
  const usuarioCreado = await objUsuario.save().catch((error) =>
    res.status(500).json({
      success: false,
      content: error,
      message: "Error al crear el usuario",
    })
  );
  return res.status(201).json({
    success: true,
    content: usuarioCreado,
    message: "Usuario Creado exitosamente",
  });
};

module.exports = {
  registro,
};
