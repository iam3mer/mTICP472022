package utp.misiontic2022.c2.p47.ejercicios;

public class AppPromedio 
{
    public static void main( String[] args ) {
        //Nota auxNota = new Nota(80);
        //auxNota.mostrarNota();

        Asignatura asignatura = new Asignatura("Programación", 
                        100, 60, 80, 75, 68);

        asignatura.calcularPromedio();
    }
}
