package utp.misiontic2022.c2.p47.unidad4_5.modelo.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.Book;
import utp.misiontic2022.c2.p47.unidad4_5.util.JDBCUtilities;

public class BookDao {

    public int validarISBN(String isbn) throws SQLException {
        int band = -1;

        String sql = "SELECT id FROM book WHERE isbn = '"+isbn+"';";

        try (
            Connection conn = JDBCUtilities.getConnection();
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
        ) {
           if (rs.next()) {
               band = rs.getInt("id");
           } 
        } 
        
        return band;
    }
    
    public Book save(Book book) throws SQLException {

        String psql = "INSERT INTO book (title,isbn,year) VALUES (?, ?, ?)";

        try (
            Connection conn = JDBCUtilities.getConnection();
            PreparedStatement pstmt = conn.prepareStatement(psql);
        ) {
            pstmt.setString(1, book.getTitle());
            pstmt.setString(2, book.getIsbn());
            pstmt.setInt(3, book.getYear());

            pstmt.executeUpdate();
            
        } 

        return book;
    }
}
