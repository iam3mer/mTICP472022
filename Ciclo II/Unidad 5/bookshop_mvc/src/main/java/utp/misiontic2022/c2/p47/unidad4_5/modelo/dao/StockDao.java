package utp.misiontic2022.c2.p47.unidad4_5.modelo.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.Stock;
import utp.misiontic2022.c2.p47.unidad4_5.util.JDBCUtilities;

public class StockDao {
    
    public Stock save(Stock stock) throws SQLException {
        String psql = "INSERT INTO stock (id_book,amount) VALUES (?, ?);";

        try (
            Connection conn = JDBCUtilities.getConnection();
            PreparedStatement pstmt = conn.prepareStatement(psql);
        ) {
            pstmt.setInt(1, stock.getId_book());
            pstmt.setInt(2, stock.getAmount());

            pstmt.executeUpdate();
        }
        return stock;
    }

    public void delete(int id_book) throws SQLException {
        String sql = "DELETE FROM stock WHERE id_book = "+id_book+";";

        try (
            Connection conn = JDBCUtilities.getConnection();
            Statement stmt = conn.createStatement();
        ){
            stmt.executeUpdate(sql);
        } 
    }

    public void update(int id_book, int unidadesVenta) throws SQLException {

        int amountUp = consultarStock(id_book) - unidadesVenta;

        String sql = "UPDATE stock SET amount = "+amountUp+" WHERE id_book = "+id_book+";";

        try (
            Connection conn = JDBCUtilities.getConnection();
            Statement stmt = conn.createStatement();
        ) {
            stmt.executeUpdate(sql);
        } 
    }

    public int consultarStock(int id_book) throws SQLException {
        int amount = 0;
        String sql = "SELECT amount FROM stock WHERE id_book = "+id_book+";";

        try (
            Connection conn = JDBCUtilities.getConnection();
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
        ) {
            if (rs.next()) {
                amount = rs.getInt("amount");
            }
        }
        return amount;
    }
}
