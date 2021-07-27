package utp.misiontic2022.c2.p47.unidad4;

import java.io.IOException;
import java.io.PrintWriter;

public class EscribeArchivo {
    public static void escribir() {
        int[][] num = {{234,234,234,34,654567,536},
                        {4,3465,345,345,345,345,345,345,34,5},
                        {3245,34,345,345,345,}};

        String file = "matriz.txt";

        try {
            PrintWriter output = new PrintWriter(file);

            for (int i = 0; i < num.length; i++) {
                for (int j = 0; j < num[i].length; j++) {
                    output.print(num[i][j] + ",");
                }
                output.println();
            }
            output.close();
        } catch (IOException e) {
            System.err.println(e);
        }
        


    }
}
