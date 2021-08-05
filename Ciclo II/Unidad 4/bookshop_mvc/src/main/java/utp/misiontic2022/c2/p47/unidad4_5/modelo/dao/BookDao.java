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

    public Book read(String isbn) throws SQLException {
        Book book = null;
        String sql = "SELECT * FROM book WHERE isbn ='"+isbn+"';";

        try (
            Connection conn = JDBCUtilities.getConnection();
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
        ) {
            if (rs.next()) {
                book = new Book();

                book.setId(rs.getInt("id"));
                book.setTitle(rs.getString("title"));
                book.setIsbn(rs.getString("isbn"));
                book.setYear(rs.getInt("year"));
            }
        }
        return book;
    }

    public boolean update(Book book) throws SQLException {
        boolean band = false;

        String sql = "UPDATE book SET title = '"+book.getTitle()+"', year = "+book.getYear()+" WHERE isbn = '"+book.getIsbn()+"';";

        try (
            Connection conn = JDBCUtilities.getConnection();
            Statement stmt = conn.createStatement();
        ) {
            int aux = stmt.executeUpdate(sql);
            if (aux > 0) {
                band = true;
            }
        } 
        return band;
    }

    public boolean delete(String isbn) throws SQLException {
        boolean band = false;

        String sql = "DELETE FROM book WHERE isbn = '"+isbn+"';";
        
        try (
            Connection conn = JDBCUtilities.getConnection();
            Statement stmt = conn.createStatement();
        ) {
            int aux = stmt.executeUpdate(sql);
            if (aux > 0) {
                band = true;
            }
        } 

        return band;
    }
}
