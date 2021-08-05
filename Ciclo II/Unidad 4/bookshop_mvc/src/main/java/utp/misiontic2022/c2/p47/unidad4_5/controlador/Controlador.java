package utp.misiontic2022.c2.p47.unidad4_5.controlador;

import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.Book;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.dao.BookDao;

import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.Stock;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.dao.StockDao;

import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.Sale;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.dao.SaleDao;

import java.sql.SQLException;

public class Controlador {

    private final BookDao bookDao;
    private final StockDao stockDao;
    private final SaleDao saleDao;

    public Controlador() {
        this.bookDao = new BookDao();
        this.stockDao = new StockDao();
        this.saleDao = new SaleDao();
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

    public boolean updateBook(String isbn, String title, int year) throws SQLException {
        boolean band;
        Book book = new Book();

        book.setTitle(title);
        book.setIsbn(isbn);
        book.setYear(year);

        band = bookDao.update(book);

        return band;
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
    
}
