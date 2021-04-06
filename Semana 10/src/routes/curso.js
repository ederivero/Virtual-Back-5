const { Router } = require("express");
const curso_controller = require("../controllers/curso");
const curso_router = Router();

curso_router
  .route("/curso")
  .post(curso_controller.crearCurso)
  .get(curso_controller.listarCursos);

curso_router
  .route("/curso/:id")
  .patch(curso_controller.actualizarCurso)
  .delete(curso_controller.eliminarCurso);

curso_router.get("/busquedaCurso", curso_controller.listarCursosPorNombre);
// curso_router.post("/curso", curso_controller.crearCurso);

module.exports = curso_router;
