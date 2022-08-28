// import file
const dotEnv = require("dotenv");

// config here
dotEnv.config();

// export here
module.exports = {
  PORT: process.env.PORT,
};
