const { DataTypes } = require("sequelize");
const { conexion } = require("../config/Sequelize");

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
  return usuario;
};
