const express = require("express");
const { json } = require("body-parser");

module.exports = class Server {
  constructor() {
    this.app = express();
    this.puerto = process.env.PORT || 5000;
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
  }
  rutas() {
    this.app.get("/", (req, res) => {
      return res
        .json({
          success: true,
          content: null,
          message: "Bievenido a mi API",
        })
        .end();
    });
  }
  start() {
    this.app.listen(this.puerto, () => {
      console.log(`Servidor corriendo en http://127.0.0.1:${this.puerto}`);
    });
  }
};
