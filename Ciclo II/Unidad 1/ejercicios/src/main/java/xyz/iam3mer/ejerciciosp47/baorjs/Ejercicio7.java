package xyz.iam3mer.ejerciciosp47.baorjs;

import java.util.Scanner;

public class Ejercicio7 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Ingrese el caracter: ");

        char caracter = input.nextLine().charAt(0);

        boolean resultado = esMayuscula(caracter);

        if (resultado) {
            System.out.printf("%c esta en mayusculas.", caracter);
        } else {
            System.out.printf("%c esta en minusculas.", caracter);
        }

    }

    public static boolean esMayuscula(char caracter) {
        if (Character.isUpperCase(caracter)) {
            return true;
        }

        return false;
    }
}
