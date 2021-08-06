package utp.misiontic2022.c2.p47.unidad4_5.vista;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLException;
import java.util.ArrayList;

import utp.misiontic2022.c2.p47.unidad4_5.controlador.Controlador;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.Book;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.BookStock;
import utp.misiontic2022.c2.p47.unidad4_5.modelo.vo.Stock;

public class Menu {
    
    private static final Controlador controlador;
    private static final BufferedReader input;

    static {
        controlador = new Controlador();
        input = new BufferedReader(new InputStreamReader(System.in));
    }

    public static void iniciar() {
        boolean loop = true;
        while (loop) {
            System.out.println("---Crud Book---");
            System.out.println("1. Crear libro");
            System.out.println("2. Leer libro");
            System.out.println("3. Actualizar libro");
            System.out.println("4. Eliminar libro");
            System.out.println("5. Vender libro");
            System.out.println("6. Salir");
            System.out.print("Ingrese una opción: ");

            try {
                String opcion = input.readLine();
                switch (opcion) {
                    case "1":
                        create();
                        break;
                    case "2":
                        read();
                        break;
                    case "3":
                        update();
                        break;
                    case "4":
                        delete();
                        break;
                    case "5":
                        sale();
                        break;
                    case "6":
                        loop = false;
                        break;
                    default:
                        System.err.println("La opción es incorrecta.");
                }

            } catch (IOException e) {
                System.err.println(e);
            }
        }
    }

    private static void create() {
        System.out.println("Creación de libro.");

        try {
            System.out.println("Ingrese el titulo: ");
            String title = input.readLine();
            System.out.println("Ingrese el isbn: ");
            String isbn = input.readLine();
            System.out.println("Ingrese el año de publicación: ");
            int year = Integer.valueOf(input.readLine());
            System.out.print("Ingrese las unidades a añadir al stock: ");
            int amount = Integer.valueOf(input.readLine());

            Book book = controlador.createBook(title, isbn, year);

            if (book != null) {
                controlador.createStock(isbn, amount);
                System.out.println("El libro se almaceno correctamente!");
            } else {
                System.out.println("El libro ya existe en la base de datos.");
            }
        } catch (IOException | SQLException e) {
            System.err.println(e);
        }
    }

    public static void read() {
        System.out.println("Leer libro.");

        try {
            System.out.print("Ingrese el isbn del libro a consultar: ");
            String isbn = input.readLine();

            Book book = controlador.readBook(isbn);

            if (book != null) {
                System.out.println(book);
            } else {
                System.out.printf("El libro con isbn %s no se encontro.", isbn);
            }

        } catch (Exception e) {
            System.err.println(e);
        }
    }

    public static void update() {
        System.out.println("Actualizar libro.");

        try {
            System.out.print("Ingrese el isbn del libro a actualizar: ");
            String isbn = input.readLine();
            System.out.print("Ingrese el titulo del libro: ");
            String title = input.readLine();
            System.out.print("Ingrese el año de publicación del libro: ");
            int year = Integer.valueOf(input.readLine());

            boolean band = controlador.updateBook(isbn, title, year);

            if (band) {
                System.out.printf("El libro con isbn %s se actualizo!\n", isbn);
            } else {
                System.out.println("No se puedo actualizar el libro.");
            }

        } catch (Exception e) {
            System.err.println(e);
        }
    }

    public static void delete() {
        System.out.println("Eliminar libro.");

        try {
            System.out.print("Ingrese el isbn del libro a eliminar: ");
            String isbn = input.readLine();

            boolean band = controlador.deleteBook(isbn);

            if (band) {
                System.out.printf("Libro con isbn %s fue eliminado!\n",isbn);
            } else {
                System.out.println("No se puede elminar el libro.");
            }

        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public static void sale() {
        System.out.println("Venta de libro.");

        try {
            ArrayList<BookStock> registrosBS = controlador.listarBS();
            for (BookStock bookStock : registrosBS) {
                System.out.printf("%s %s %d (%d)\n",
                    bookStock.getIsbn(),
                    bookStock.getTitle(),
                    bookStock.getYear(),
                    bookStock.getAmount()
                );
            }

            System.out.print("Ingrese el isbn del libro a comprar: ");
            String isbn = input.readLine();
            System.out.print("Ingrese el numero de unidades a comprar: ");
            int unidadesVenta = Integer.valueOf(input.readLine());

            boolean venta = controlador.venderLibro(isbn, unidadesVenta);

            if (venta) {
                System.out.printf("Se vendieron %d unidades de %s\n",unidadesVenta,isbn);
            } else {
                System.out.printf("No hay suficientes unidades del libro %s para realizar la venta!\n",isbn);
            }
        } catch (Exception e) {
            System.err.println(e);
        }
    }

}
