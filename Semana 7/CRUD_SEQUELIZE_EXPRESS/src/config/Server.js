const express = require('express');
const {json} = require('body-parser');
const {conexion} = require('./Sequelize');
const categoria_model = require('../models/Categoria');
const cliente_model = require('../models/Cliente')
module.exports = class Server{
    constructor(){
        this.app = express()
        this.puerto = process.env.PORT || 5000;
        this.bodyParser();
        this.CORS()
        this.rutas()
    }
    bodyParser(){
        this.app.use(json())
    }
    CORS(){
        // los cors son el control de acceso a nuestra api, aca definimos que dominios pueden acceder, que metodos se pueden acceder y que headers se puede enviar
        this.app.use((req, res, next)=>{
            // Access-Control-Allow-Origin => indica que dominio o dominios pueden acceder a mi API
            res.header('Access-Control-Allow-Origin', '*')
            // Access-Control-Allow-Headers => sirve para indicar que tipos de cabeceras me puede mandar el front
            res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
            // Access-Control-Allow-Methods => sirve para indicar que metodos pueden acceder a mi API
            res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
            // si todo cumple con lo solicitado pasara al siguiente controlador
            next()
        })
    }
    rutas(){
        this.app.get('/',(req, res)=>{
            res.json({
                message:'Bienvenido a mi API 😎'
            })
        })
    }
    start(){
        this.app.listen(this.puerto, async()=>{
            console.log(`Servidor corriendo exitosamente en el puerto ${this.puerto}`);
            try {
                // si usamos algun parametro del sync en la conexion se ejecutara para todas los modelos que tengamos registrado en nuestro proyecto (CUIDADO!!!)
                // dentro del sync se puede pasar un parametro con dos llaves:
                // force => va a resetear toda la tabla o bd, va a borrar toda su configuracion y va a crear todo de 0, se perdera toda la data correspondiente (internamente hace un drop table y un create table if not exists)
                // alter => verifica que los modelos esten igual que las tablas en al bd y si hay algun cambio como tipo de dato, nombre de columna, etc solamente hara ese cambio mas no reseteará la(s) tabla(s) como lo hace el force, (internamente hace un alter table)
                // basta con llamar al modelo este se encargara de su creacion
                const Categoria = categoria_model();
                cliente_model()
                // el metodo sync es el encargado de hacer la validacion entre mi proyecto y mi bd y verificar que todas las tablas que tengo en mi proyecto esten presentes en la bd
                let respuesta = await conexion.sync({force:true})
                // console.log(respuesta.config)
                console.log('Base de datos sincronizada correctamente')
                
            } catch (error) {
                console.log(error)
            }
        })
    }
}
