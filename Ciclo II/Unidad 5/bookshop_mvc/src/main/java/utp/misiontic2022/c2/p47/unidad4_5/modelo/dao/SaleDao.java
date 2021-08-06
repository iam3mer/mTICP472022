package utp.misiontic2022.c2.p47.unidad4_5.modelo.dao;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import utp.misiontic2022.c2.p47.unidad4_5.util.JDBCUtilities;

public class SaleDao {
    
    public boolean validarVenta (String isbn) throws SQLException {
        boolean band = true;

        String sql = "SELECT count() as sale FROM sales s JOIN book b WHERE s.id_book = b.id AND b.isbn = '"+isbn+"';";
        
        try (
            Connection conn = JDBCUtilities.getConnection();
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
        ) {
            if (rs.next()) {
                if (rs.getInt("sale") == 0) {
                    band = false;
                }
            }
        } 
        return band;
    }

    public int vender(int id_book, int unidadesVenta) throws SQLException {
        String sql = "INSERT INTO sales VALUES (DATETIME('now'), "+id_book+", "+unidadesVenta+");";

        try (
            Connection conn = JDBCUtilities.getConnection();
            Statement stmt = conn.createStatement();
        ) {
            return stmt.executeUpdate(sql);
        } 
    }
}
