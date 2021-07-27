package utp.misiontic2022.c2.p47.unidad4;

import java.io.File;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        /*
        File archivo = new File("archivo.txt");

        System.out.println(archivo.getPath());
        System.out.println(archivo.getAbsolutePath());
        System.out.println(archivo.getName());
        System.out.println(archivo.isFile());
        System.out.println(archivo.isDirectory());
        System.out.println(archivo.length());
        System.out.println(archivo.exists());
        */

        EscribeArchivo.escribir();
        LeeArchivo.leer();
    }
}
