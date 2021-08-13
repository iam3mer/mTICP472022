/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package utp.misiontic2022.c2.p47.unidad4_5.vista;

import java.util.ArrayList;
import java.util.List;
import javax.swing.table.AbstractTableModel;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.BookStock;

/**
 *
 * @author 3mer
 */
public class BookStockTM extends AbstractTableModel{
        
    private List<BookStock> booksStocks;
    
    public BookStockTM() {
        this(new ArrayList<>());
    }
    
    public BookStockTM(List<BookStock> booksStocks) {
        this.booksStocks = booksStocks;
    }
    
    public void addBook(BookStock bs) {
        booksStocks.add(bs);
        fireTableDataChanged();
    }
    
    public void removeBook(int row) {
        booksStocks.remove(row);
        fireTableDataChanged();
    }
    
    public void setBook(int row, BookStock bs) {
        booksStocks.set(row, bs);
        fireTableDataChanged();
    }
    
    public BookStock getBook(int row) {
        return booksStocks.get(row);
    }

    @Override
    public String getColumnName(int column) {
        switch(column) {
            case 0:
                return "ID";
            case 1:
                return "Nombre";
            case 2:
                return "ISBN";
            case 3:
                return "Año";
            case 4:
                return "Amount";
        }
        return super.getColumnName(column);
    }
    
    @Override
    public int getRowCount() {
        return booksStocks.size();
    }

    @Override
    public int getColumnCount() {
        return 5;
    }

    @Override
    public Object getValueAt(int row, int column) {
        BookStock bs = booksStocks.get(row);
        switch(column) {
            case 0:
                return bs.getId();
            case 1:
                return bs.getTitle();
            case 2:
                return bs.getIsbn();
            case 3:
                return bs.getYear();
            case 4:
                return bs.getAmount();
        }
        return null;
    }
}
