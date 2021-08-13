package utp.misiontic2022.c2.p47.unidad4_5.controlador;

import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.Book;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.dao.BookDao;

import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.Stock;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.dao.StockDao;

import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.Sale;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.dao.SaleDao;

import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.BookStock;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.dao.BookStockDao;

import java.sql.SQLException;
import java.util.ArrayList;

public class Controlador {

    private final BookDao bookDao;
    private final StockDao stockDao;
    private final SaleDao saleDao;
    private final BookStockDao bookstockDao;

    public Controlador() {
        this.bookDao = new BookDao();
        this.stockDao = new StockDao();
        this.saleDao = new SaleDao();
        this.bookstockDao = new BookStockDao();
    }

    public Book createBook(String title, String isbn, int year) throws SQLException {
        Book book = null;
        int band = 0;

        try {
            band = bookDao.validarISBN(isbn);

            if (band == -1) {
                book = new Book();
    
                book.setTitle(title);
                book.setIsbn(isbn);
                book.setYear(year);
                
                book = bookDao.save(book);
            }
        }  finally {}
        return book;
    }

    public Book readBook (String isbn) throws SQLException {
        Book book = bookDao.read(isbn);
        return book;
    }

    public boolean deleteBook(String isbn) throws SQLException {
        boolean delete = false;

        int aux = bookDao.validarISBN(isbn);

        if (aux != -1) {
            boolean band = saleDao.validarVenta(isbn);
            if (band == false) {
                int id_book = bookDao.read(isbn).getId();
                delete = bookDao.delete(isbn);
                if (delete) {
                    stockDao.delete(id_book);
                }
            }
        }

        return delete;
    }

    public Book updateBook(String isbn, String title, int year) throws SQLException {
        //boolean band;
        Book book = new Book();

        book.setTitle(title);
        book.setIsbn(isbn);
        book.setYear(year);

        //band = bookDao.update(book);
        bookDao.update(book);

        return book;
    }

    public ArrayList<Book> findAllBooks() throws SQLException {
        return bookDao.allBooks();
    }

    public void createStock(String isbn, int amount) throws SQLException {
        int id_book = readBook(isbn).getId();
        createStock(id_book, amount);
    }

    public void createStock(int id_book, int amount) throws SQLException {
        Stock stock = new Stock();

        stock.setId_book(id_book);
        stock.setAmount(amount);

        stockDao.save(stock);
    }

    public ArrayList<BookStock> listarBS () throws SQLException {
        return bookstockDao.consultarBS();
    }
    
    public ArrayList<BookStock> listarTodosBS () throws SQLException {
        return bookstockDao.consultarTodosBS();
    }

    public boolean venderLibro(String isbn, int unidadesVenta) throws SQLException {
        boolean venta = false;

        int id_book = bookDao.validarISBN(isbn);
        if (id_book > 0) {
            //int id_book = bookDao.read(isbn).getId();
            int stock = stockDao.consultarStock(id_book);

            if (stock > unidadesVenta) {
                int auxV = saleDao.vender(id_book, unidadesVenta);
                if (auxV > 0) {
                    stockDao.update(id_book, unidadesVenta);
                }
                venta = true;
            }
        }
        return venta;
    }
    
}
