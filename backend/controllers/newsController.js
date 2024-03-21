const NewsArticle = require("../models/newsarticleModel");
const mongoose = require("mongoose");

//get all
const getNews = async (req, res) => {
  const newsArticles = await NewsArticle.find({}).sort({ createdAt: -1 });

  res.status(200).json({ newsArticles });
};

//create
const createNews = async (req, res) => {
  const { title, url, date } = req.body;

  //adds to db
  try {
    const newsArticle = await NewsArticle.create({ title, url, date }); // Added await here
    res.status(200).json({ newsArticle });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

// delete
const deleteNews = async (req, res) => {
  const { id } = req.params;

  if (!mongoose.Types.ObjectId.isValid(id)) {
    return res.status(404).send("No news with that id");
  }

  const news = await NewsArticle.findOneAndDelete({ _id: id });

  if (!news) {
    return res.status(400).json({ error: "No such workout" });
  }
  res.status(200).json(news);
};

// update
const updateNews = async (req, res) => {
  const { id } = req.params;

  if (!mongoose.Types.ObjectId.isValid(id)) {
    return res.status(404).send("No news with that id");
  }

  const news = await NewsArticle.findOneAndUpdate(
    { _id: id },
    {
      ...req.body,
    }
  );

  if (!news) {
    return res.status(400).json({ error: "No such workout" });
  }
  res.status(200).json(news);
};
//exports
module.exports = {
  getNews,
  createNews,
  deleteNews,
  updateNews,
};
