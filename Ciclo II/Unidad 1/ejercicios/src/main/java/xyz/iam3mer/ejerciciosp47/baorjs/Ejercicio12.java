package xyz.iam3mer.ejerciciosp47.baorjs;

public class Ejercicio12 {
    public static void main(String[] args) {
        Integer limite = 100;

        System.out.println("for");
        for (int i = 1; i <= limite; i++) {
            if (i % 3 != 0) {
                System.out.printf("%d ", i);
            }
        }

        System.out.printf("\nwhile\n");
        Integer i = 1;
        while (i <= limite) {
            if (i % 3 != 0) {
                System.out.printf("%d ", i);
            }
            ++i;
        }

        System.out.printf("\ndo-while\n");
        i = 1;
        do {
            if (i % 3 != 0) {
                System.out.printf("%d ", i);
            }
            ++i;
        } while (i <= limite);
    }
}
