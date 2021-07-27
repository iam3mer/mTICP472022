package utp.misiontic2022.c2.p47.unidad4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class IO_3 {
    public static void iniciar() {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter output = new PrintWriter(System.out, true);

        String line = null;

        output.println("Ingrese un texto:");
        try {
            line = input.readLine();
        } catch (IOException e) {
            System.err.println(e);
        }

        output.println("El texto es:");
        output.println(line);
    }
}
