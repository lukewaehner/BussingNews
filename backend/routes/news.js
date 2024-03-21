const express = require("express");
const NewsArticle = require("../models/newsarticleModel");
const {
  createNews,
  getNews,
  deleteNews,
  updateNews,
} = require("../controllers/newsController");

const router = express.Router();

//get all
router.get("/", getNews);

//delete
router.delete("/:id", deleteNews);

//post
router.post("/", createNews);

//patch
router.patch("/:id", updateNews);

module.exports = router;
