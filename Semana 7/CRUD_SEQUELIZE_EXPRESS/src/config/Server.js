const express = require("express");
const { json } = require("body-parser");
const { conexion } = require("./Sequelize");
const categoria_model = require("../models/Categoria");
const cliente_model = require("../models/Cliente");
const usuario_model = require("../models/Usuario");
const cabecera_model = require("../models/Cabecera");
const producto_model = require("../models/Producto");
const detalle_model = require("../models/Detalle");
const promocion_model = require("../models/Promocion");
module.exports = class Server {
  constructor() {
    this.app = express();
    this.puerto = process.env.PORT || 5000;
    this.bodyParser();
    this.CORS();
    this.rutas();
  }
  bodyParser() {
    this.app.use(json());
  }
  CORS() {
    // los cors son el control de acceso a nuestra api, aca definimos que dominios pueden acceder, que metodos se pueden acceder y que headers se puede enviar
    this.app.use((req, res, next) => {
      // Access-Control-Allow-Origin => indica que dominio o dominios pueden acceder a mi API
      res.header("Access-Control-Allow-Origin", "*");
      // Access-Control-Allow-Headers => sirve para indicar que tipos de cabeceras me puede mandar el front
      res.header("Access-Control-Allow-Headers", "Content-Type, Authorization");
      // Access-Control-Allow-Methods => sirve para indicar que metodos pueden acceder a mi API
      res.header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
      // si todo cumple con lo solicitado pasara al siguiente controlador
      next();
    });
  }
  rutas() {
    this.app.get("/", (req, res) => {
      res.json({
        message: "Bienvenido a mi API 😎",
      });
    });
  }
  crearTablas() {
    // si usamos algun parametro del sync en la conexion se ejecutara para todas los modelos que tengamos registrado en nuestro proyecto (CUIDADO!!!)
    // dentro del sync se puede pasar un parametro con dos llaves:
    // force => va a resetear toda la tabla o bd, va a borrar toda su configuracion y va a crear todo de 0, se perdera toda la data correspondiente (internamente hace un drop table y un create table if not exists)
    // alter => verifica que los modelos esten igual que las tablas en al bd y si hay algun cambio como tipo de dato, nombre de columna, etc solamente hara ese cambio mas no reseteará la(s) tabla(s) como lo hace el force, (internamente hace un alter table)
    // basta con llamar al modelo este se encargara de su creacion
    const Categoria = categoria_model();
    const Cliente = cliente_model();
    const Usuario = usuario_model();
    const CabeceraNota = cabecera_model();
    const Producto = producto_model();
    const Detalle = detalle_model();
    const Promocion = promocion_model();
    // una vez definidos todos los modelos pasamos a crear sus relaciones
    // Usuario tiene muchos Cabecera nota
    // si deseamos cambiar el nombre x defecto tenemos que registrar su 'foreignKey': 'nombre', pero si deseamos agregar campos como no permitir que pueda ser nula esa fk, debemos abrir un objeto dentro de foreignKey e indicar dichas propiedades
    Usuario.hasMany(CabeceraNota, {
      foreignKey: { name: "usu_id", allowNull: false },
    });
    // Cabecera Nota pertenece a un Usuario
    CabeceraNota.belongsTo(Usuario, { foreignKey: "usu_id" });

    Cliente.hasMany(CabeceraNota, {
      foreignKey: { name: "cli_dni", allowNull: false },
    });
    CabeceraNota.belongsTo(Cliente, { foreignKey: "cli_dni" });

    CabeceraNota.hasMany(Detalle, {
      foreignKey: { name: "cab_id", allowNull: false },
    });
    Detalle.belongsTo(CabeceraNota, { foreignKey: "cab_id" });

    Producto.hasMany(Detalle, {
      foreignKey: { name: "prod_id", allowNull: false },
    });
    Detalle.belongsTo(Producto, { foreignKey: "prod_id" });

    Categoria.hasMany(Producto, {
      foreignKey: { name: "cat_id", allowNull: false },
    });
    Producto.belongsTo(Categoria, { foreignKey: "cat_id" });

    Producto.hasMany(Promocion, {
      foreignKey: { name: "prod_id", allowNull: false },
    });
    Promocion.belongsTo(Producto, { foreignKey: "prod_id" });
  }
  start() {
    this.app.listen(this.puerto, async () => {
      console.log(
        `Servidor corriendo exitosamente en el puerto ${this.puerto}`
      );
      try {
        this.crearTablas();
        // el metodo sync es el encargado de hacer la validacion entre mi proyecto y mi bd y verificar que todas las tablas que tengo en mi proyecto esten presentes en la bd
        let respuesta = await conexion.sync({force: true});
        // console.log(respuesta.config)
        console.log("Base de datos sincronizada correctamente");
      } catch (error) {
        console.log(error);
      }
    });
  }
};
