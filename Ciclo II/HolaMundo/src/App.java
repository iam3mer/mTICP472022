import java.util.Scanner;

public class HolaMundo {
    public static void main(String[] args) throws Exception {
    
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingresa tu apellido: ");
        String apellido = sc.nextLine();

        System.out.println("Hello, "+args[0]+" "+apellido+"!");
    }
}
