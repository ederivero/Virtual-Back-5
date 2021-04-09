require("dotenv").config();
const express = require("express");
const { json, text } = require("body-parser");
const mongoose = require("mongoose");
const curso_router = require("../routes/curso");
const usuario_router = require("../routes/usuario");
const comentario_router = require("../routes/comentario");
const imagen_router = require("../routes/imagen");
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
    this.app.use(
      curso_router,
      usuario_router,
      imagen_router,
      comentario_router
    );
  }
  async conectarMongoDb() {
    // mongodb://localhost:27017/plataforma_educativa
    await mongoose
      .connect(process.env.MONGO_COMPASS, {
        useNewUrlParser: true, // para indicar que estamos usando el nuevo formato de coneccion url
        useUnifiedTopology: true, // para indicar que vamos a usar un nuevo motor de administracion de conecciones, solamente indicar false cuando la conexion sea poco estable
        useCreateIndex: true, // para indicar que haga la creacion de indices de las collecciones de la bd
        useFindAndModify: false, // sirve para indicar que los metodos findOneAndUpdate y findOneAndDelete no se usaran porque ya son deprecados (obsoletos)
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
