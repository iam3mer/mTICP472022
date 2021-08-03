package utp.misiontic2022.c2.p47.unidad4_5.controlador;

import java.sql.SQLException;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.Book;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.dao.BookDao;

public class Controlador {

    private final BookDao bookDao;

    public Controlador() {
        this.bookDao = new BookDao();
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
    
}
