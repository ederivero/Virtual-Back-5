import express from "express";
import { Server } from "http";
import socketIo from "socket.io";

export default class ServidorSocket {
  constructor() {
    this.app = express();
    this.puerto = process.env.PORT || 3000;
    this.httpServer = new Server(this.app);
    this.io = socketIo(this.httpServer, {
      // https://socket.io/docs/v4/handling-cors/
      cors: {
        origin: "*",
      },
    });
    this.escucharSocket();
    this.rutas();
  }
  escucharSocket() {
    let usuarios = [];
    const mensajes = [];
    this.io.on("connect", (cliente) => {
      this.io.emit("lista-usuarios", usuarios);
      // console.log(cliente);
      console.log(`Se conecto el cliente ${cliente.id}`);
      cliente.on("disconnect", (motivo) => {
        // este socket se ejecuta automaticamente cuando el usuario se desconecta
        console.log(`Se desconecto el cliente ${cliente.id}`);
        console.log(motivo);
        // filtrame todos los usuarios siempre y cuando el id del usuario no sea igual que el id del usuario que se acaba de desconectar
        usuarios = usuarios.filter((usuario) => usuario.id !== cliente.id);
        // una vez que retiramos al usuario del array ahora hacemos la emision de la nueva lista de usuarios
        this.io.emit("lista-usuarios", usuarios);
        // transport close => cuando el cliente cierra sesion o cierra pestaña
        // ping timeout => cuando el tiempo de espera es demasiado prolongado
      });
      cliente.on("configurar-cliente", (nombre) => {
        // se puede recibir lo que sea = un obj, un array, cualquer variable
        console.log(nombre);
        usuarios.push({
          id: cliente.id,
          nombre,
        });
        this.io.emit("lista-usuarios", usuarios);
      });

      cliente.on("mensaje", (mensaje) => {
        const usuario = usuarios.filter(
          (usuario) => usuario.id === cliente.id
        )[0];
        mensajes.push({
          cliente: usuario.nombre,
          mensaje,
        });
        // si nosotros queremos emitir al mismo cliente que se ha conectado usaremos su metodo cliente,emit()
        // si queremos emitir a todos los demas EXCEPTO a la persona que ha enviado el evento que desencana el emit usuremos cliente.broadcast.emit()
        // si queremos emitir a todos los usuario conectados al socket usaremos el objeto del socket this.io.emit() NOTA=> en el objeto this.io no existe el metodo broadcast()
        this.io.emit("lista-mensajes", mensajes);
      });
    });
  }
  rutas() {
    this.app.get("/", (req, res) => {
      res.json({
        success: true,
        content: null,
        message: "Bienvenido a mi app de sockets 🔌",
      });
    });
  }
  start() {
    this.httpServer.listen(this.puerto, () => {
      console.log(
        `Servidor corriendo exitosamente en http://127.0.0.1:${this.puerto}`
      );
    });
  }
}
