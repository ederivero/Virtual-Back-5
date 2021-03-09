const { Sequelize } = require("sequelize");

// 1ra forma es usando la URI
// const conexion = new Sequelize("mysql://usuario:password@host:puerto/base_datos",
//   {
//     dialect: "mysql",
//     timezone: "-05:00",
//     dialectOptions: {
//       // sirve para que al momento de mostrar fechas, automaticamente las vuelva string y no tener que hacer la conversion manual como en flask
//       dateString: true,
//     },
//   }
// );

// 2da forma es dando detalles de conexion
const conexion = new Sequelize(
  // base datos , usuario, password
  "minimarket",
  "root",
  "root",
  {
    host: "localhost",
    dialect: "mysql",
    timezone: "-05:00",
    dialectOptions: {
      // sirve para que al momento de mostrar fechas, automaticamente las vuelva string y no tener que hacer la conversion manual como en flask
      dateStrings: true,
    },
  }
);

/* aqui van a ir las declaraciones de los modelos */

module.exports={
    conexion
}