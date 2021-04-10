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
// el metodo emit sirve para enviar algo al back mediante el nombre de su socket
ingresar.addEventListener("click", (e) => {
  e.preventDefault();
  socket.emit("configurar-cliente", nombre.value);
  ingresar.disabled = true;
  nombre.disabled = true;
});
socket.on("lista-usuarios", (usuarios) => {
  console.log(usuarios);
  listaUsuarios.innerHTML = "";
  for (const key in usuarios) {
    const usuarioLi = document.createElement("li");
    usuarioLi.className = "list-group-item";
    usuarioLi.innerText = usuarios[key].nombre;
    listaUsuarios.appendChild(usuarioLi);
  }
});

mensaje.addEventListener("keyup", (e) => {
  // console.log(e.key);
  if (e.key === "Enter") {
    socket.emit("mensaje", mensaje.value);
    mensaje.value = "";
  }
});

socket.on("lista-mensajes", (mensajes) => {
  listaMensaje.innerHTML = "";
  mensajes.forEach((mensaje) => {
    const mensajeLi = document.createElement("li");
    mensajeLi.className = "list-group-item";
    mensajeLi.innerText = `${mensaje.cliente} dice: ${mensaje.mensaje}`;
    listaMensaje.appendChild(mensajeLi);
  });
});
