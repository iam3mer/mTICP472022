const mongoose = require("mongoose");

const booksSchema = mongoose.Schema({
  isbn: String,
  title: String,
  autores: Array,
  descripcion: String,
  portada: String,
})

module.exports = mongoose.model("books", booksSchema);