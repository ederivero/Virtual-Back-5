const { Schema } = require("mongoose");
const moment = require("moment-timezone");
const { imagenSchema } = require("./imagen");
// https://es.wikipedia.org/wiki/ISO_3166-2
const fechaPeruana = moment.tz(Date.now(), "America/Lima");

const contenidoSchema = new Schema(
  {
    // un curso puede tener varios videos , entonces crear el videoSchema en el cual se tendra: vide_url (string y requerido), video_orden (numerico, requerido y no admite valores negativos), video_nombre (string, y no puede tener mas de 80 caracteres)
    video_url: {
      type: String,
      required: true,
    },
    video_orden: {
      type: Number,
      required: true,
      min: 0,
    },
    video_nombre: {
      type: String,
      maxlength: 80,
    },
  },
  { _id: false }
);

const cursoSchema = new Schema({
  // https://mongoosejs.com/docs/schematypes.html#schematype-options
  curso_nombre: {
    type: String,
    unique: true,
    required: true,
    uppercase: true,
    maxlength: 50,
  },
  curso_descripcion: String,
  curso_link: String,
  curso_fecha_lanzamiento: {
    type: Date,
    min: "2021-01-01",
    max: "2021-03-31 23:59",
    default: fechaPeruana,
  },
  curso_imagenes: [imagenSchema],
  curso_videos: [contenidoSchema],
  curso_publicado: {
    type: Boolean,
    default: false,
  },
  curso_duracion: String,
  curso_costo: {
    type: Schema.Types.Decimal128, // se puede usar los tipos de datos nativos de JS o usar los provenientes de Schema.Types.
    min: 0,
  },
  usuarios: [Schema.Types.ObjectId],
  comentarios: [Schema.Types.ObjectId],
});

module.exports = {
  cursoSchema,
};
