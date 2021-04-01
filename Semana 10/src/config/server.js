const express = require("express");
const { json, text } = require("body-parser");
const mongoose = require("mongoose");

module.exports = class Server {
  constructor() {
    this.app = express();
    this.puerto = process.env.PORT || 5000;
    this.CORS();
    this.bodyParser();
    this.rutas();
    this.conectarMongoDb();
  }
  CORS() {
    this.app.use((req, res, next) => {
      res.header("Access-Control-Allow-Origin", "*");
      res.header("Access-Control-Allow-Header", "Content-Type, Authorization");
      res.header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
      next();
    });
  }
  bodyParser() {
    this.app.use(json());
    this.app.use(text());
  }
  rutas() {
    this.app.get("/", (req, res) => {
      console.log(req.body);
      return res
        .json({
          success: true,
          content: null,
          message: "Bievenido a mi API",
        })
        .end();
    });
  }
  async conectarMongoDb() {
    await mongoose
      .connect("mongodb://localhost:27017/plataforma_educativa", {
        useNewUrlParser: true, // para indicar que estamos usando el nuevo formato de coneccion url
        useUnifiedTopology: true, // para indicar que vamos a usar un nuevo motor de administracion de conecciones, solamente indicar false cuando la conexion sea poco estable
        // para ver que otras opciones se pueden asignar => https://mongoosejs.com/docs/connections.html#options
      })
      .catch((e) => console.error(e));
    console.log("Base de datos conectada exitosamente");
  }
  start() {
    this.app.listen(this.puerto, () => {
      console.log(`Servidor corriendo en http://127.0.0.1:${this.puerto}`);
    });
  }
};
