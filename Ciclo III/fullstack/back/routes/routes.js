const express = require("express");

const BooksController = require("../controllers/BooksController");

const router = express.Router();

// Rutes Books
router.get('/books', BooksController.getAllBooks);
router.get('/books/isbn/:isbn', BooksController.getBookByIsbn);
router.get('/books/title/:titulo', BooksController.getBookByTitulo);
router.post('/books', BooksController.insert);
router.put('/books/isbn/:isbn', BooksController.update);
router.delete('/books/isbn/:isbn', BooksController.delete);

module.exports = router;