const {
  subirArchivo,
  eliminarArchivo,
} = require("../utils/manejadorFirebaseStorage");

const subirImagen = async (req, res) => {
  console.log(req.file);
  const archivo = req.file;
  const link = await subirArchivo(archivo).catch((error) =>
    res.json({
      success: false,
      content: null,
      message: error,
    })
  );
  return res.json({
    succes: true,
    content: link,
    message: "Imagen subida exitosamente",
  });
};

const eliminarImagen = async (req, res) => {
  const { nombre } = req.query;
  const respuesta = await eliminarArchivo(nombre);
  if (respuesta) {
    res.json({
      success: true,
      content: null,
      message: "Archivo eliminado exitosamente",
    });
  } else {
    res.status(400).json({
      success: true,
      content: null,
      message: "Error al eliminar el archivo",
    });
  }
};

module.exports = { subirImagen, eliminarImagen };
