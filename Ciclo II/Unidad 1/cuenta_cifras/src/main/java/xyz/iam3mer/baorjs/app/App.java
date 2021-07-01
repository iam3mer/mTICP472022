package xyz.iam3mer.baorjs.app;

import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {

        Scanner input = new Scanner(System.in);

        System.out.println( "Ingrese un numero: " );

        int numero = input.nextInt();

        int numeroCifras = contarCifras(numero);

        System.out.printf("\nEl numero %d tiene %d cifra(s).", numero, numeroCifras);

        input.close();

    }

    public static int contarCifras(int numero)
    {
        int cifras = numero == 0 ? 1 : 0;

        while (numero != 0)
        {
            numero /= 10;
            ++cifras;
        }

        return cifras;
    }

}
