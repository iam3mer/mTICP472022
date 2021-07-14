package utp.misiontic2022.c2.p47.ejercicios;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {   
        PruebaThrow operacion = new PruebaThrow();

        try{
            operacion.divide0(3, 0);
        } catch (ArithmeticException ex) {
            System.out.println("No se puede dividir entre 0");
        }
        
        /*
        try {
            System.out.println(57/2);
            Integer[] array = {1,"S"};
        } catch (ArithmeticException ex) {
            System.out.println("No se puede dividir entre cero. " + ex.getMessage());
        } catch (Error | ArrayIndexOutOfBoundsException ex){
            //System.out.println("Esta tratando de acceder a un indice que no existe.");
            System.out.println("Hay un problema con el array");
        } finally {
            System.out.println("Este bloque siempre se ejecuta.");
        }
        */
    }
}
