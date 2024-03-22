const mongoose = require("mongoose");

const Schema = mongoose.Schema;
const newsSchema = new Schema(
  {
    //needs this schema
    title: {
      type: String,
      required: true,
    },

    url: {
      type: String,
      required: true,
    },

    date: {
      type: Number,
      // need to figure out how to parse dates, should be simple but building out everything first
    },
    source: {
      type: String,
    },
    //
  },
  { timestamps: true }
);

module.exports = mongoose.model("NewsArticle", newsSchema);
// Path: backend/routes/news.js
