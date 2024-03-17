const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
  res.json({ message: "get news dummy response" });
});

module.exports = router;
