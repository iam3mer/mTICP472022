/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package utp.misiontic2022.c2.p47.unidad4_5.vista;

import java.awt.HeadlessException;
import java.sql.SQLException;
import javax.swing.JOptionPane;
import javax.swing.ListSelectionModel;
import utp.misiontic2022.c2.p47.unidad4_5.controlador.Controlador;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.Book;

/**
 *
 * @author 3mer
 */
public class Bookshop_GUI extends javax.swing.JFrame {
    
    private Controlador controlador;
    private BookTM bookTM;
    private BookStockTM bookStockTM;

    /**
     * Creates new form Bookshop_GUI
     */
    public Bookshop_GUI() {
        controlador = new Controlador();
        initComponents();
        listarLibros();
        listarStock();
        setLocationRelativeTo(null);
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        tpPrincipal = new javax.swing.JTabbedPane();
        pBook = new javax.swing.JPanel();
        jLabel2 = new javax.swing.JLabel();
        jSplitPane2 = new javax.swing.JSplitPane();
        jPanel1 = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        idBook = new javax.swing.JTextField();
        jLabel3 = new javax.swing.JLabel();
        txtTitle = new javax.swing.JTextField();
        jLabel4 = new javax.swing.JLabel();
        txtIsbn = new javax.swing.JTextField();
        jLabel5 = new javax.swing.JLabel();
        txtYear = new javax.swing.JTextField();
        btnAddBook = new javax.swing.JButton();
        jPanel2 = new javax.swing.JPanel();
        jPanel3 = new javax.swing.JPanel();
        btnNewBook = new javax.swing.JButton();
        btnDeleteBook = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        tblBooks = new javax.swing.JTable();
        pStock = new javax.swing.JPanel();
        jLabel6 = new javax.swing.JLabel();
        spStock = new javax.swing.JSplitPane();
        jPanel4 = new javax.swing.JPanel();
        jPanel5 = new javax.swing.JPanel();
        jScrollPane2 = new javax.swing.JScrollPane();
        tblBookStock = new javax.swing.JTable();
        pSale = new javax.swing.JPanel();
        barMenu = new javax.swing.JMenuBar();
        mArchivo = new javax.swing.JMenu();
        miSalir = new javax.swing.JMenuItem();
        mVentanas = new javax.swing.JMenu();
        miBooks = new javax.swing.JMenuItem();
        miStock = new javax.swing.JMenuItem();
        miSales = new javax.swing.JMenuItem();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("BookShop");
        setMinimumSize(new java.awt.Dimension(600, 300));

        pBook.setLayout(new java.awt.BorderLayout());

        jLabel2.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel2.setText("Gestión de Libros");
        pBook.add(jLabel2, java.awt.BorderLayout.PAGE_START);

        jSplitPane2.setDividerLocation(35);
        jSplitPane2.setOrientation(javax.swing.JSplitPane.VERTICAL_SPLIT);
        jSplitPane2.setEnabled(false);

        jLabel1.setText("ID:");

        idBook.setEditable(false);
        idBook.setEnabled(false);
        idBook.setFocusable(false);

        jLabel3.setText("Nombre:");

        txtTitle.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtTitleActionPerformed(evt);
            }
        });

        jLabel4.setText("ISBN:");

        jLabel5.setText("Año");

        btnAddBook.setText("Guardar");
        btnAddBook.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnAddBookActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabel1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(idBook, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel3)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(txtTitle, javax.swing.GroupLayout.PREFERRED_SIZE, 264, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel4)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(txtIsbn, javax.swing.GroupLayout.PREFERRED_SIZE, 161, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel5)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(txtYear, javax.swing.GroupLayout.PREFERRED_SIZE, 50, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(btnAddBook)
                .addContainerGap(11, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel1)
                    .addComponent(idBook, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel3)
                    .addComponent(txtTitle, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel4)
                    .addComponent(txtIsbn, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel5)
                    .addComponent(txtYear, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(btnAddBook))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        jSplitPane2.setLeftComponent(jPanel1);

        jPanel2.setLayout(new java.awt.BorderLayout());

        jPanel3.setLayout(new java.awt.FlowLayout(java.awt.FlowLayout.RIGHT));

        btnNewBook.setText("Nuevo");
        btnNewBook.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnNewBookActionPerformed(evt);
            }
        });
        jPanel3.add(btnNewBook);

        btnDeleteBook.setText("Eliminar");
        btnDeleteBook.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnDeleteBookActionPerformed(evt);
            }
        });
        jPanel3.add(btnDeleteBook);

        jPanel2.add(jPanel3, java.awt.BorderLayout.PAGE_END);

        tblBooks.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null}
            },
            new String [] {
                "Title 1", "Title 2", "Title 3", "Title 4"
            }
        ));
        jScrollPane1.setViewportView(tblBooks);

        jPanel2.add(jScrollPane1, java.awt.BorderLayout.CENTER);

        jSplitPane2.setRightComponent(jPanel2);

        pBook.add(jSplitPane2, java.awt.BorderLayout.CENTER);

        tpPrincipal.addTab("Book", pBook);

        pStock.setLayout(new java.awt.BorderLayout());

        jLabel6.setText("jLabel6");
        pStock.add(jLabel6, java.awt.BorderLayout.PAGE_START);

        spStock.setDividerLocation(35);
        spStock.setOrientation(javax.swing.JSplitPane.VERTICAL_SPLIT);

        javax.swing.GroupLayout jPanel4Layout = new javax.swing.GroupLayout(jPanel4);
        jPanel4.setLayout(jPanel4Layout);
        jPanel4Layout.setHorizontalGroup(
            jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 763, Short.MAX_VALUE)
        );
        jPanel4Layout.setVerticalGroup(
            jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 35, Short.MAX_VALUE)
        );

        spStock.setLeftComponent(jPanel4);

        jPanel5.setLayout(new java.awt.BorderLayout());

        tblBookStock.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null, null},
                {null, null, null, null, null},
                {null, null, null, null, null},
                {null, null, null, null, null}
            },
            new String [] {
                "Title 1", "Title 2", "Title 3", "Title 4", "Title 5"
            }
        ));
        jScrollPane2.setViewportView(tblBookStock);

        jPanel5.add(jScrollPane2, java.awt.BorderLayout.CENTER);

        spStock.setRightComponent(jPanel5);

        pStock.add(spStock, java.awt.BorderLayout.CENTER);

        tpPrincipal.addTab("Stock", pStock);
        tpPrincipal.addTab("Sale", pSale);

        getContentPane().add(tpPrincipal, java.awt.BorderLayout.CENTER);

        mArchivo.setText("Archivo");

        miSalir.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_Q, java.awt.event.InputEvent.CTRL_DOWN_MASK));
        miSalir.setText("Salir");
        miSalir.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                miSalirActionPerformed(evt);
            }
        });
        mArchivo.add(miSalir);

        barMenu.add(mArchivo);

        mVentanas.setText("Ventanas");

        miBooks.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_B, java.awt.event.InputEvent.CTRL_DOWN_MASK));
        miBooks.setText("Books");
        miBooks.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                miBooksActionPerformed(evt);
            }
        });
        mVentanas.add(miBooks);

        miStock.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_S, java.awt.event.InputEvent.CTRL_DOWN_MASK));
        miStock.setText("Stock");
        miStock.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                miStockActionPerformed(evt);
            }
        });
        mVentanas.add(miStock);

        miSales.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_LESS, java.awt.event.InputEvent.CTRL_DOWN_MASK));
        miSales.setText("Sales");
        miSales.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                miSalesActionPerformed(evt);
            }
        });
        mVentanas.add(miSales);

        barMenu.add(mVentanas);

        setJMenuBar(barMenu);

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void miBooksActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_miBooksActionPerformed
        tpPrincipal.setSelectedIndex(0);
    }//GEN-LAST:event_miBooksActionPerformed

    private void miSalesActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_miSalesActionPerformed
        tpPrincipal.setSelectedIndex(2);
    }//GEN-LAST:event_miSalesActionPerformed

    private void miStockActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_miStockActionPerformed
        tpPrincipal.setSelectedIndex(1);
    }//GEN-LAST:event_miStockActionPerformed

    private void miSalirActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_miSalirActionPerformed
        exit_app();
    }//GEN-LAST:event_miSalirActionPerformed

    private void listarLibros() {
        
        txtIsbn.setEnabled(false);
        idBook.setEditable(false);
        
        try {
            var books = controlador.findAllBooks();
            bookTM = new BookTM(books);
            tblBooks.setModel(bookTM);
            
            tblBooks.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
            tblBooks.getSelectionModel().addListSelectionListener((e) -> {
                var row = tblBooks.getSelectedRow();
                if (row == -1) {
                    limpiarCamposLibro();
                } else {
                    var book = bookTM.getBook(row);
                    cargarCamposLibro(book);
                }
            });
        } catch (Exception e) {
        }
    }
    
    private void listarStock() {
        
        try {
            var bs = controlador.listarTodosBS();
            bookStockTM = new BookStockTM(bs);
            tblBookStock.setModel(bookStockTM);
        } catch (Exception e) {
        }
    }
    
    public void cargarCamposLibro(Book book) {
        idBook.setText(String.valueOf(book.getId()));
        txtTitle.setText(book.getTitle());
        txtIsbn.setText(book.getIsbn());
        txtYear.setText(String.valueOf(book.getYear()));
        btnAddBook.setText("Actualizar");
    }
    
    private void exit_app() throws HeadlessException {
        if (JOptionPane.showConfirmDialog(this, "Desea cerrar la aplicación?",
                getTitle(), JOptionPane.YES_OPTION) == JOptionPane.YES_OPTION) {
            dispose();
        }
    }
    
    private void txtTitleActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtTitleActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtTitleActionPerformed

    private void btnNewBookActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnNewBookActionPerformed
        limpiarCamposLibro();
        btnAddBook.setText("Guardar");
        txtIsbn.setEnabled(true);
        txtTitle.requestFocus();
    }//GEN-LAST:event_btnNewBookActionPerformed

    private void btnAddBookActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnAddBookActionPerformed
        if (txtTitle.getText().trim().isBlank()) {
            JOptionPane.showMessageDialog(this, "El titulo es obligatorio!", getTitle(), JOptionPane.WARNING_MESSAGE);
            txtTitle.requestFocus();
        }
        
        if (txtIsbn.getText().trim().isBlank()) {
            JOptionPane.showMessageDialog(this, "El ISBN es obligatorio!", getTitle(), JOptionPane.WARNING_MESSAGE);
            txtIsbn.requestFocus();
        }
        
        if (txtYear.getText().trim().isBlank()) {
            JOptionPane.showMessageDialog(this, "El año es obligatorio!", getTitle(), JOptionPane.WARNING_MESSAGE);
            txtYear.requestFocus();
        }
        
        try {
            String id = idBook.getText();
            String title = txtTitle.getText().trim();
            String isbn = txtIsbn.getText().trim();
            Integer year = Integer.valueOf(txtYear.getText());
            
            if (id.isBlank()) {
                var book = controlador.createBook(title, isbn, year);
                if (book != null) {
                    bookTM.addBook(book);
                    limpiarCamposLibro();
                    JOptionPane.showMessageDialog(this, "El libro se guardo!");
                } else {
                    JOptionPane.showMessageDialog(this, "No se puede guardar el libro!");
                }
            } else {
                var row = tblBooks.getSelectedRow();
                var book = controlador.updateBook(isbn, title, year);
                if (book != null) {
                    book.setId(Integer.valueOf(id));
                    bookTM.setBook(row, book);
                }
            }
            
        } catch (SQLException e) {
            JOptionPane.showMessageDialog(this, "Error: No se pudo ejecutar la acción!", getTitle(), JOptionPane.ERROR_MESSAGE);
        }
        
    }//GEN-LAST:event_btnAddBookActionPerformed

    private void btnDeleteBookActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnDeleteBookActionPerformed
        if (JOptionPane.showConfirmDialog(this,
                "Esta seguro de elminar el libro?\nEl libro solo se elimina si no hay ventas del mismo!",
                getTitle(),
                JOptionPane.YES_NO_OPTION,
                JOptionPane.WARNING_MESSAGE) == JOptionPane.YES_OPTION) {
            
            var row = tblBooks.getSelectedRow();
            
            try {
                var delete = controlador.deleteBook(txtIsbn.getText());
                if (delete) {
                    bookTM.removeBook(row);
                    JOptionPane.showMessageDialog(this, "El libro se elimino!");
                } else {
                    JOptionPane.showMessageDialog(this, "No se puede eliminar un libro con ventas!");
                }
            } catch (SQLException e) {
                JOptionPane.showMessageDialog(this, "Error: No se puedo realizar la acción", getTitle(), JOptionPane.ERROR_MESSAGE);
            }
        }
    }//GEN-LAST:event_btnDeleteBookActionPerformed

    private void limpiarCamposLibro() {
        idBook.setText("");
        txtTitle.setText("");
        txtIsbn.setText("");
        txtYear.setText("");
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Bookshop_GUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Bookshop_GUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Bookshop_GUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Bookshop_GUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Bookshop_GUI().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JMenuBar barMenu;
    private javax.swing.JButton btnAddBook;
    private javax.swing.JButton btnDeleteBook;
    private javax.swing.JButton btnNewBook;
    private javax.swing.JTextField idBook;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JPanel jPanel4;
    private javax.swing.JPanel jPanel5;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JSplitPane jSplitPane2;
    private javax.swing.JMenu mArchivo;
    private javax.swing.JMenu mVentanas;
    private javax.swing.JMenuItem miBooks;
    private javax.swing.JMenuItem miSales;
    private javax.swing.JMenuItem miSalir;
    private javax.swing.JMenuItem miStock;
    private javax.swing.JPanel pBook;
    private javax.swing.JPanel pSale;
    private javax.swing.JPanel pStock;
    private javax.swing.JSplitPane spStock;
    private javax.swing.JTable tblBookStock;
    private javax.swing.JTable tblBooks;
    private javax.swing.JTabbedPane tpPrincipal;
    private javax.swing.JTextField txtIsbn;
    private javax.swing.JTextField txtTitle;
    private javax.swing.JTextField txtYear;
    // End of variables declaration//GEN-END:variables
}
