const { DataTypes } = require("sequelize");
const { conexion } = require("../config/Sequelize");
const bcrypt = require("bcrypt");

module.exports = usuario_model = () => {
  let usuario = conexion.define(
    "usuarios",
    {
      usuarioId: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        field: "usu_id",
        allowNull: false,
        primaryKey: true,
        unique: true,
      },
      usuarioEmail: {
        type: DataTypes.STRING(45),
        field: "usu_email",
        unique: true,
        // https://sequelize.org/master/manual/validations-and-constraints.html
        validate: {
          isEmail: true,
          len: [5, 45],
        },
      },
      usuarioSuperuser: {
        type: DataTypes.BOOLEAN,
        field: "usu_superuser",
        defaultValue: false,
      },
      usuarioPassword: {
        type: DataTypes.TEXT,
        field: "usu_password",
        allowNull: false,
      },
    },
    {
      timestamps: false,
      tableName: "t_usuario",
    }
  );
  /** Aqui ira la encriptacion de la contraseña */
  // al momento de usar el prototype estamos agregando nuevas funcionalidades a nuestro objecto usuario para que puedan ser usadas como el findAll(), build(), etc. estas podran ser accedidas desde cualquier lado de la app
  usuario.prototype.setearPassword = function (password) {
    // Por si se desea guardar el salt en la bd
    // bcrypt.genSaltSync(10)
    const hash = bcrypt.hashSync(password, 10);
    this.usuarioPassword = hash;
  };
  usuario.prototype.validarPassword = function (password) {
    // comparar la contraseña que se le provee con el hash almacenado y si son iguales retornara Verdadero, caso contrario retornara Falso
    return bcrypt.compareSync(password, this.usuarioPassword);
  };
  return usuario;
};
