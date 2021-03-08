const express = require('express');
const {json} = require('body-parser');

module.exports = class Server{
    constructor(){
        this.app = express()
        this.puerto = process.env.PORT || 5000;
        this.bodyParser();
        this.rutas()
    }
    bodyParser(){
        this.app.use(json())
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
