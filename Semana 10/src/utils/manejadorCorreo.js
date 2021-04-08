const nodeMailer = require("nodemailer");

const clienteCorreo = nodeMailer.createTransport({
  host: "smtp.gmail.com",
  port: 587,
  secure: false, // secure va a ser true cuando el puerto sea el 465
  auth: {
    user: "testappseduardo@gmail.com",
    pass: "Pruebas2020",
  },
  tls: {
    rejectUnauthorized: false,
  },
});

const enviarCorreo = (para, titulo, cuerpo) => {
  return new Promise((resolve, reject) => {
    clienteCorreo
      .sendMail({
        to: para,
        subject: titulo,
        text: cuerpo,
      })
      .then((resultado) => resolve(resultado))
      .catch((error) => reject(error));
  });
};

module.exports = { enviarCorreo };
