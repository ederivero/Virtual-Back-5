const { Schema } = require("mongoose");
const { imagenSchema } = require("./imagen");

const telefonoSchema = new Schema({
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
});

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
      minlength: 25,
      unique: true,
    },
    usuario_hash: String,
    usuario_categoria: {
      type: Number,
      min: 1,
      max: 4,
    },
    usuario_telefono: [telefonoSchema],
    usuario_imagen: imagenSchema,
    // String, Number, Date, Buffer, Boolean, Mixed, ObjectId, Array, Decimal128, Map, Schema
  },
  {
    timestamps: {
      createdAt: "fecha_creacion",
      updatedAt: "fecha_actualizacion",
    },
  }
);

module.exports = {
  usuarioSchema,
};
