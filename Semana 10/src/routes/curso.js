const { Router } = require("express");
const curso_controller = require("../controllers/curso");
const curso_router = Router();

curso_router.route("/curso").post(curso_controller.crearCurso);
// curso_router.post("/curso", curso_controller.crearCurso);

module.exports = curso_router;
