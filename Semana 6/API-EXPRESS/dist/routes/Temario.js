// esto se llama destructuracion y sirve para solamente usar una parte de una libreria, documento, etc.
const {Router} = require('express')
const {crearTemario} = require('../controllers/Temario')

const temario_router = Router();
temario_router.post('/temario', crearTemario)

module.exports = temario_router