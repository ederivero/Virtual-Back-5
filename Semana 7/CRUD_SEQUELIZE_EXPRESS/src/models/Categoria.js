const { DataTypes } = require('sequelize')
// const {conexion} = require('../config/Sequelize')
// https://sequelize.org/master/manual/model-basics.html#column-options
module.exports =  categoria_model = (conexion)=>{
    return categoria = conexion.define('categoria', {
        categoriaId: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            allowNull: false,
            autoIncrement: true,
            field: 'cat_id'
        }
    })
}

// module.exports = categoria_model