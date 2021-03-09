const express = require('express');
const {json} = require('body-parser');

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
        this.app.listen(this.puerto, ()=>{
            console.log(`Servidor corriendo exitosamente en el puerto ${this.puerto}`);
        })
    }
}
