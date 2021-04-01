const { model } = require("mongoose");
const { usuarioSchema } = require("../models/usuario");

const Usuario = model("usuario", usuarioSchema);

module.exports = {
  Usuario,
};
