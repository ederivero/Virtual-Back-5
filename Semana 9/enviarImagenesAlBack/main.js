const nombre = document.getElementById("inputNombre");
const cantidad = document.getElementById("inputCantidad");
const precio = document.getElementById("inputPrecio");
const foto = document.getElementById("inputFoto");
const registrar = document.getElementById("btnRegistrar");
const mostrar = document.getElementById("btnMostrar");
const informacion = document.getElementById("platos");
const BASE_URL = "http://127.0.0.1:8000";

// creo este objeto para poder mandarselo al back
const formData = new FormData();
registrar.addEventListener("click", async (e) => {
  e.preventDefault();
  formData.append("platoDescripcion", nombre.value);
  formData.append("platoCantidad", cantidad.value);
  formData.append("platoPrecio", precio.value);
  // el input file siempre guardar los files en forma de un array , aun asi solo se le pase 1
  formData.append("platoFoto", foto.files[0]);
  const resultado = await fetch(BASE_URL + "/plato", {
    method: "POST",
    body: formData,
    // ejemplo para pasar una token (o cualquier header)
    headers: {
      Authorization: "Bearer 123123.123123.123123",
    },
  });
  const json = await resultado.json();
  console.log(json);
});

mostrar.addEventListener("click", async (e) => {
  e.preventDefault();
  const resultado = await fetch(BASE_URL + "/plato", {
    method: "GET",
  });
  const json = await resultado.json();

  informacion.innerText = JSON.stringify(json);
});
