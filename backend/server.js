require("dotenv").config();

const express = require("express");
const newsRoutes = require("./routes/news");
const mongoose = require("mongoose");

//app
const app = express();

//middleware if needed

//reactions / routes
app.use("/api/news/", newsRoutes);

//connect to db
mongoose
  .connect(process.env.MONGO_URI)
  .then(() => {
    // listen for requests when in DB
    app.listen(process.env.PORT, () => {
      console.log(
        "Connected to DB & Server is listening on port",
        process.env.PORT
      );
    });
  })
  .catch((error) => {
    console.log(error);
  });
