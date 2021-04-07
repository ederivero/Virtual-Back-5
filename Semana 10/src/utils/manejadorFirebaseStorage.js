const { Storage } = require("@google-cloud/storage");
// Inicializamos el objeto de firebase para poder conectarme al bucket (almacenamiento)
const storage = new Storage({
  projectId: "prueba-firebase-eduardo",
  keyFilename: "./credenciales_firebase.json",
});

// se crea la variable bucket que se usa como referencia al link del storage
// ! No se copia el protocolo, solamente despues del doble slash '//'
const bucket = storage.bucket("prueba-firebase-eduardo.appspot.com");

const subirArchivo = (archivo) => {
  return new Promise((resolve, reject) => {
    // validamos que tengamos un archivo si es que no hay hacemos un rechazo
    if (!archivo) reject("No se encontro el archivo");
    // comenzamos a cargar el archivo mediante su nombre
    const fileUpload = bucket.file(archivo.originalname);
    // agregamos configuracion adicional de nuestro archivo a subir como x ejemplo su metadata
    const blobStream = fileUpload.createWriteStream({
      metadata: {
        contentType: archivo.mimetype,
      },
    });
    // si hay un error al momento de subir el archivo ingresaremos a su estado "error"
    blobStream.on("error", (error) => {
      reject(`Hubo un error al subir el archivo: ${error}`);
    });
    // si el archivo termino de subirse correctametne ingresaremos a su estado "finish"
    blobStream.on("finish", () => {
      fileUpload
        .getSignedUrl({
          action: "read",
          expires: "04-10-2021", // MM-DD-YYYY
        })
        .then((link) => resolve(link))
        .catch((error) => reject(error));
    });
    // aca es donde se culmina el proceso de subida de imagenes
    // se le manda el buffer del archivo (los bytes del archivo)
    blobStream.end(archivo.buffer);
  });
};

module.exports = { subirArchivo };
