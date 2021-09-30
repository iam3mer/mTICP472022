const booksModel = require("../models/BooksModel");

module.exports = class BooksController {

  static async getAllBooks (request, response) {
    try {
      const books = await booksModel.find();
      response.status(200).json(books);
    } catch (error) {
      response.status(400).json({message: error.message});
    }
  };

  static async getBookByTitulo (request, response) {
    try {
      const titulo = request.params.titulo;
      const book = await booksModel.find({title: titulo});
      if (book != null) {
        response.status(200).json(book);
      } else {
        response.status(404).json();
      }
    } catch (error) {
      response.status(400).json({message: error.message});
    }
  };

  static async getBookByIsbn (request, response) {
    try {
      const isbn = request.params.isbn;
      const book = await booksModel.find({isbn: isbn});
      if (book != null) {
        response.status(200).json(book);
      } else {
        response.status(404).json();
      }
    } catch (error) {
      response.status(400).json({message: error.message});
    }
  };

  static async delete (request, response) {
    try {
      const isbn = request.params.isbn;
      await booksModel.deleteOne({isbn: isbn});
      response.status(200).json();
    } catch (error) {
      response.status(400).json({message: error.message});
    }
  };

  static async insert (request, response) {
    try {
      const document = request.body;
      // Validar la estructura del documento y el tipo de dato
      const book = await booksModel.create(document);
      response.status(200).json(book);
    } catch (error) {
      response.status(400).json({message: error.message});
    }
  };

  static async update (request, respose) {
    try {
      const isbn = request.params.isbn;
      const data = request.body;
      const book = await booksModel.updateOne({isbn: isbn}, data);
      respose.status(200).json(book);
    } catch (error) {
      respose.status(400).json({message: error.message});
    }
  };

}