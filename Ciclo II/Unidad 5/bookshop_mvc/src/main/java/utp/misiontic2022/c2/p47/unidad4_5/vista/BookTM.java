/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package utp.misiontic2022.c2.p47.unidad4_5.vista;

import java.util.ArrayList;
import java.util.List;
import javax.swing.table.AbstractTableModel;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.Book;

/**
 *
 * @author 3mer
 */
public class BookTM extends AbstractTableModel{
    
    private List<Book> books;
    
    public BookTM() {
        this(new ArrayList<>());
    }
    
    public BookTM(List<Book> books) {
        this.books = books;
    }
    
    public void addBook(Book book) {
        books.add(book);
        fireTableDataChanged();
    }
    
    public void removeBook(int row) {
        books.remove(row);
        fireTableDataChanged();
    }
    
    public void setBook(int row, Book book) {
        books.set(row, book);
        fireTableDataChanged();
    }
    
    public Book getBook(int row) {
        return books.get(row);
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
        }
        return super.getColumnName(column);
    }
    
    

    @Override
    public int getRowCount() {
        return books.size();
    }

    @Override
    public int getColumnCount() {
        return 4;
    }

    @Override
    public Object getValueAt(int row, int column) {
        Book book = books.get(row);
        switch(column) {
            case 0:
                return book.getId();
            case 1:
                return book.getTitle();
            case 2:
                return book.getIsbn();
            case 3:
                return book.getYear();
        }
        return null;
    }
    
}
