const { Router } = require("express");
const usuario_controller = require("../controllers/usuario");
const { wachiman } = require("../utils/validador");
const usuario_router = Router();

usuario_router.post("/registro", usuario_controller.registro);
usuario_router.post("/login", usuario_controller.login);
usuario_router.post("/inscribir", wachiman, usuario_controller.inscribirCurso);

module.exports = usuario_router;
