// import file here
const express = require("express");
const { PORT } = require("./config");
const { DatabaseConnection } = require("./database");
const AppExress = require("./express-app");

// main function
const StartServer = async () => {
  //  app is start
  const app = express();

  // connect the database
  await DatabaseConnection();

  await AppExress(app);

  // app is listening here
  app
    .listen(PORT, () => {
      console.log(`listening on port ${PORT}`);
    })
    .on("error", (err) => {
      console.log(err);
      process.exit();
    });
};

// main function starting here
StartServer();
