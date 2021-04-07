const { Usuario, Curso } = require("../config/mongoose");
const { subirArchivo } = require("../utils/manejadorFirebaseStorage");

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

const login = async (req, res) => {
  const { email, password } = req.body;
  const usuarioEncontrado = await Usuario.findOne({
    usuario_email: email,
  }).catch((error) =>
    res.status(500).json({
      success: false,
      content: error,
      message: "Error al buscar el usuario",
    })
  );
  if (!usuarioEncontrado) {
    return res.status(404).json({
      success: false,
      content: null,
      message: "Correo no se encuentra",
    });
  }
  if (usuarioEncontrado.validarPassword(password)) {
    return res.json({
      success: true,
      content: usuarioEncontrado.generarJWT(),
      message: "Logeado correctamente",
    });
  } else {
    return res.status(404).json({
      success: false,
      content: null,
      message: "Contraseña incorrecta",
    });
  }
};

const inscribirCurso = async (req, res) => {
  /**
   * 1. usar la token para ver que usuario esta queriendo acceder a que curso ✔
   * 2. mediante la url indicar el id del curso (query) 127.0.0.1:5000/inscribir?id=12121212121
   * 2.1 ver si el curso existe
   * 3. ver si el usuario ya esta inscrito en el curso y si lo esta no permitir volver a inscribirlo
   * 4. si no esta inscrito, inscribirlo
   */
  const curso_id = req.query.id;
  const { usuario_id } = req.usuario;
  const cursoEncontrado = await Curso.findById(curso_id).catch((error) => {
    res.status(404).json({
      success: false,
      content: error,
      message: "No se encontro el curso",
    });
  });
  if (cursoEncontrado) {
    const usuarioEncontrado = await Usuario.findById(usuario_id);
    const resultado = usuarioEncontrado.cursos.includes(curso_id);
    if (resultado && cursoEncontrado.usuarios.includes(usuario_id)) {
      return res.status(401).json({
        success: false,
        content: null,
        message: "Curso ya se encuentra registrado en el Usuario",
      });
    }
    usuarioEncontrado.cursos.push(curso_id);
    usuarioEncontrado.save();

    // ahora ingresar ese usuario en el schema cursos => usuarios:[]
    cursoEncontrado.usuarios.push(usuario_id);
    cursoEncontrado.save();

    return res.status(201).json({
      success: true,
      content: usuarioEncontrado,
      message: "Usuario enrolado exitosamente",
    });
  }
};

// mostrar los cursos del usuario
// nombre, descripcion, link, imagenes
const mostrarCursosUsuario = async (req, res) => {
  const { usuario_id } = req.usuario;
  // iterar los cursos del usuario y buscarlos en la coleccion de cursos
  const { cursos } = await Usuario.findById(usuario_id);
  console.log(cursos);
  let resultado = [];
  let resultado2;
  // 1ra forma
  resultado2 = await Promise.all(
    cursos.map((curso) =>
      Curso.findById(
        curso,
        "curso_nombre curso_descripcion curso_link curso_imagenes"
      )
    )
  );
  console.log(resultado2);
  // 2da forma
  for (const key in cursos) {
    resultado.push(
      await Curso.findById(
        cursos[key],
        "curso_nombre curso_descripcion curso_link curso_imagenes"
      )
    );
  }
  return res.json({
    success: true,
    content: resultado2,
    message: null,
  });
};

const editarUsuario = async (req, res) => {
  // * TAREA IMPLEMENTAR ESTE CONTROLADOR
  const { usuario_id } = req.usuario;
  const link = await subirArchivo(req.file).catch((error) =>
    res.json({
      success: false,
      content: error,
      message: "Error al subir la imagen",
    })
  );
  if (link) {
    if (req.body.usuario_password) delete req.body.usuario_password;
    req.body.usuario_imagen = { imagen_url: link[0] };
    const usuarioActualizado = await Usuario.findByIdAndUpdate(
      usuario_id,
      req.body,
      { new: true }
    );
    return res.json({
      success: true,
      content: usuarioActualizado,
      message: null,
    });
  }
};

const cambiarPassword = async (req, res) => {
  const { usuario_id } = req.usuario;
  const { newPassword, oldPassword } = req.body;
  // validar si la oldPassword es la contraseña actual
  // si lo es, cambiar la contraseña (encriptacion)
  // si no lo es, indicar que no se pudo cambiar la password
};

const resetPassword = async (req, res) => {};

module.exports = {
  registro,
  login,
  inscribirCurso,
  mostrarCursosUsuario,
  editarUsuario,
};
