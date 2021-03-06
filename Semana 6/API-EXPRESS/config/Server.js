// npm i express
const express = require("express"); // esta es la forma de importar librerias y archivos en js

class Server {
  constructor() {
    // creo una instancia de la clase Express
    this.app = express();
    // hace una busqueda en las variables de entorno de la variable PORT y si no hay indica que el puerto sera el 5000
    this.puerto = process.env.PORT || 5000;   
    this.rutas();
  }
  rutas(){
      // encargado de configurar todas las rutas de mi aplicacion
      this.app.get('/',(req, res)=>{
          // el request es todo lo que me manda el cliente
          // el response es la forma en la cual le respondo
          console.log('El cliente me llama!')
          return res.status(200).send('Bienvenido a mi API')
      })
  }

  iniciarServidor() {
    // se queda escuchando al servidor que se levanta mediante un determinado puerto
    this.app.listen(this.puerto, () => {
      console.log(
        `El servidor se ha levantado exitosamente en el puerto ${this.puerto}`
      );
    });
  }
}
// export default
module.exports = Server
