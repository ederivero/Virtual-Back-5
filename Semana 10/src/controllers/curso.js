const { Curso } = require("../config/mongoose");

const crearCurso = async (req, res) => {
  try {
    // Forma 1 : en dos pasos
    const nuevoCurso = new Curso(req.body);
    // aqui ira la logica de subida de imagenes
    const cursoCreado = await nuevoCurso.save();
    // Forma 2 : en un solo paso
    // const cursoCreado2 = await Curso.create(req.body);
    // Forma 3: insertar varios registros
    // Curso.insertMany(req.body) // req.body => deberia ser un array de objetos de cursos
    return res.status(201).json({
      success: true,
      content: cursoCreado,
      message: "Curso creado exitosamente",
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      content: error,
      message: "Error al crear el curso",
    });
  }
};

module.exports = {
  crearCurso,
};
