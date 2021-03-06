// esto se llama destructuracion y sirve para solamente usar una parte de una libreria, documento, etc.
const {Router} = require('express')
// PRIMER METODO
// const {crearTemario, devolverTemarios, actualizarTemario} = require('../controllers/Temario')
// SEGUNDO METODO
const temarioController = require('../controllers/Temario')

const temario_router = Router();
temario_router.post('/temario', temarioController.crearTemario)
temario_router.get('/temario', temarioController.devolverTemarios)
temario_router.put('/temario/:id', temarioController.actualizarTemario)
temario_router.delete('/temario/:id', temarioController.eliminarTemario)
module.exports = temario_router