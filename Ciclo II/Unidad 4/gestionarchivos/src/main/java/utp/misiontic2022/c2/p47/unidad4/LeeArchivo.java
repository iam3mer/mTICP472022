package utp.misiontic2022.c2.p47.unidad4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.StringTokenizer;

public class LeeArchivo {
    public static void leer() {
        String nomFile = "matriz.txt";

        File file = new File(nomFile);

        if (file.exists()) {
            try {
                Scanner input = new Scanner(file);

                while (input.hasNext()) {
                    StringTokenizer num = new StringTokenizer(input.next(), ",");
                    while (num.hasMoreTokens()) {
                        System.out.print(num.nextToken() + "\t");
                    }
                    System.out.println();
                }
                input.close();
            } catch (FileNotFoundException e) {
                System.err.println(e);
            }
        } else {
            System.out.println("El archivo no existe!");
        }
    }
}
