const mongoose = require("mongoose");

const restaurantsSchema = mongoose.Schema({
  "address": Object,
  "borough": String,
  "cuisine": String,
  "grades": Array,
  "name": String,
  "restaurant_id": String
});

module.exports = mongoose.model("Restaurants", restaurantsSchema);