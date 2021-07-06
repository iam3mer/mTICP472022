package utp.misiontic2022.c2.p47.notas;

import java.util.function.DoubleBinaryOperator;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {

        Double auxNota = Double.parseDouble(args[0]);

        for (int i = 1; i < args.length; i++) {
            if (Double.parseDouble(args[i]) < auxNota) {
                auxNota = Double.parseDouble(args[i]);
            }
        }

        System.out.println(auxNota);
    }
}
