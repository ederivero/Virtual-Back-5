const { Router } = require("express");
const comentario_controller = require("../controllers/comentario");
const { wachiman } = require("../utils/validador");

const comentario_router = Router();

//...

module.exports = comentario_router;
