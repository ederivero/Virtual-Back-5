const { DataTypes } = require('sequelize')
const {conexion} = require('../config/Sequelize')
// https://sequelize.org/master/manual/model-basics.html#column-options
module.exports = categoria_model = ()=>{
    return categoria = conexion.define('categoria', {
        categoriaId: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            allowNull: false, // no puede permitir valores nulos
            autoIncrement: true, // es autoincrementable
            field: 'cat_id' // el nombre de esa columna en la tabla de la bd
        },
        categoriaNombre:{
            type: DataTypes.STRING(45),
            unique: true,
            allowNull: false,
            field: 'cat_nombre'
        }
    },{
        tableName: 't_categoria',
        timestamps: false
    })
}

// module.exports = categoria_model