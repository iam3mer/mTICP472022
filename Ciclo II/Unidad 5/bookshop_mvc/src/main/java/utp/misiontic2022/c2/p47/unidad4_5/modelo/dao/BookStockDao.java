package utp.misiontic2022.c2.p47.unidad4_5.modelo.dao;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.BookStock;
import utp.misiontic2022.c2.p47.unidad4_5.util.JDBCUtilities;

public class BookStockDao {
    
    public ArrayList<BookStock> consultarBS() throws SQLException {
        ArrayList<BookStock> registrosBS = new ArrayList<>();
        BookStock registroBS = null;

        String sql = "SELECT isbn, title, year, amount "
                    +"FROM book b JOIN stock s "
                    +"ON b.id = s.id_book "
                    +"WHERE s.amount > 0;";

        try (
            Connection conn = JDBCUtilities.getConnection();
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
        ) {
            while (rs.next()) {
                registroBS = new BookStock();

                registroBS.setIsbn(rs.getString("isbn"));
                registroBS.setTitle(rs.getString("title"));
                registroBS.setYear(rs.getInt("year"));
                registroBS.setAmount(rs.getInt("amount"));

                registrosBS.add(registroBS);
            }
        } 

        return registrosBS;
    }
    
    public ArrayList<BookStock> consultarTodosBS() throws SQLException {
        ArrayList<BookStock> registrosBS = new ArrayList<>();
        BookStock registroBS = null;

        String sql = "SELECT id, title, isbn, year, amount " +
                    "FROM book b LEFT JOIN stock s " +
                    "ON b.id = s.id_book;";

        try (
            Connection conn = JDBCUtilities.getConnection();
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
        ) {
            while (rs.next()) {
                registroBS = new BookStock();

                registroBS.setId(rs.getInt("id"));
                registroBS.setIsbn(rs.getString("isbn"));
                registroBS.setTitle(rs.getString("title"));
                registroBS.setYear(rs.getInt("year"));
                registroBS.setAmount(rs.getInt("amount"));

                registrosBS.add(registroBS);
            }
        } 

        return registrosBS;
    }
}
