const { Schema } = require("mongoose");
const { hashSync, compareSync } = require("bcrypt");
const { sign } = require("jsonwebtoken");
const { imagenSchema } = require("./imagen");
require("dotenv").config();

const telefonoSchema = new Schema(
  {
    fono_codigo: {
      type: Number,
      min: 1,
      max: 99,
    },
    fono_numero: {
      type: String,
      minlength: 6,
      maxlength: 10,
    },
  },
  {
    _id: false,
  }
);

const usuarioSchema = new Schema(
  {
    usuario_nombre: {
      type: String,
      required: true,
      alias: "usu_nomb",
    },
    usuario_apellido: {
      type: String,
      maxlength: 25,
    },
    usuario_email: {
      type: String,
      maxlength: 50,
      minlength: 10,
      unique: true,
    },
    usuario_password: String,
    usuario_categoria: {
      type: Number,
      min: 1,
      max: 4,
    },
    usuario_password_recovery: {
      type: String,
      required: false,
    },
    usuario_telefono: [telefonoSchema],
    usuario_imagen: imagenSchema,
    cursos: [Schema.Types.ObjectId],
    comentarios: [Schema.Types.ObjectId],
    // String, Number, Date, Buffer, Boolean, Mixed, ObjectId, Array, Decimal128, Map, Schema
  },
  {
    timestamps: {
      createdAt: "fecha_creacion",
      updatedAt: "fecha_actualizacion",
    },
  }
);

usuarioSchema.methods.encriptarPassword = function (password) {
  this.usuario_password = hashSync(password, 10);
};

usuarioSchema.methods.validarPassword = function (password) {
  return compareSync(password, this.usuario_password);
};

usuarioSchema.methods.generarJWT = function () {
  const payload = {
    usuario_id: this._id,
  };
  const password = process.env.JWT_SECRET;
  return sign(payload, password, { expiresIn: "1h" }, { algorithm: "RS256" });
};

module.exports = {
  usuarioSchema,
};
