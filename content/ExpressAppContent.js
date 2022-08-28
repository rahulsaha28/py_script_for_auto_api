// import
const express = require("express");
const cors = require("cors");
const BodyParsee = require("body-parser");
const { BaseError } = require("./utils");

//export express app
module.exports = async (app) => {
  app.use(BodyParsee.urlencoded({ extended: true }));
  app.use(express.json({ limit: "1mb" }));
  app.use(cors());

  //api : like: product(app)

  // base errors
  app.use(BaseError);
};
