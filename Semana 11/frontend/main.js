const socket = io("http://127.0.0.1:3000");
const nombre = document.getElementById("nombre");
const ingresar = document.getElementById("ingresar");
const listaUsuarios = document.getElementById("lista-usuarios");
const mensaje = document.getElementById("mensaje");
const listaMensaje = document.getElementById("lista-mensajes");
// el nombre connect sirve para conectarnos al socket (y el backend recibira la notificacion de la nueva conexion)
// el metodo on sirve para mandar algo al back
socket.on("connect", () => {
  console.log("conectado");
});
// el metodo emit sirve para recibir lo que el back nos esta mandando
