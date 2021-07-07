package utp.misiontic2022.c2.p47.notas_oop;

public class App 
{
    public static void main( String[] args )
    {
        //Asignatura Asignatura = new Asignatura("Programación",50,80,90,40,100);

        Nota nota = new Nota(40);

        System.out.println(nota.mostrarNota());
    }
}
