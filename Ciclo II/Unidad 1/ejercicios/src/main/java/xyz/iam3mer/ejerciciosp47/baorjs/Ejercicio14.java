package xyz.iam3mer.ejerciciosp47.baorjs;

import java.util.Scanner;

public class Ejercicio14 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Ingrese la cantidad de terminos de fibonacci que desea ver: ");
        Integer N = input.nextInt();

        input.close();

        Integer f1 = 0;
        Integer f2 = 1;

        if (N == 1) {
            System.out.println(f1);
        }

        else if (N == 2) {
            System.out.printf("%d %d", f1, f2);
        }
        else {
            Integer cont = 0;
            System.out.printf("%d %d ", f1, f2);
            while (cont < N) { // Que cambia para mostrar los primeros N numeros de la serie?
                cont=f2;
                f2+=f1;
                f1=cont;
                System.out.printf("%d ",f2);

            }
        }

    }
}
