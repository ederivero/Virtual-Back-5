const { Usuario } = require("../config/Relaciones");
// Registro
const registro = async (req, res) => {
  // vamos a utilizar la creacion en dos pasos
  // 1. contruimos el objeto usuario
  const { password } = req.body;
  const nuevoUsuario = Usuario.build(req.body);
  nuevoUsuario.setearPassword(password);
  // 2. una vez realizadas las modificaciones a nuestro objeto, procedemos a guardarlo en la bd
  await nuevoUsuario.save();
  return res.status(201).json({
    success: true,
    content: nuevoUsuario,
    message: "Usuario creado exitosamente",
  });
};
// Login
const login = async (req, res) => {
  const { email, password } = req.body;
  // 1. validar si el correo existe
  // await Usuario.find...
  // 2. validar si la contraseña existe
  // usuarioEncontrado.validarPassword(password) <- retorna un booleano (V -> si es, F -> si no es)
};

module.exports = {
  registro,
  login,
};
