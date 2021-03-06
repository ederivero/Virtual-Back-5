// let funcionar en el scope actual y no es reconocido fuera de el
// var funciona de manera global en el documento
// const funciona como una constante en la cual no se puede cambiar su valor despues de definirlo
let temario = [];
const crearTemario = (req, res)=>{
    // el request sirve para recibir todo lo que el usuario nos este mandando
    console.log(req.body);
    return res.json({
        success: true
    })
}
const devolverTemarios = (req, res)=>{}

module.exports={
    crearTemario,
    devolverTemarios
}