package utp.misiontic2022.c2.p47.unidad4;

import java.util.Arrays;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        WritePeople.write(
            "people.data",
            Arrays.asList(
                new People("Andres", "Barbosa", "Bogota", 20),
                new People("Carlos", "Figueroa", "Manizales", 21),
                new People("Nelsi", "Miramag", "Barranquilla", 20),
                new People("Andres", "Garcia", "Manizales", 22)
            )
        );
        
        ReadPeople rp = new ReadPeople();
        rp.read();
        System.out.printf("La suma de las edades es: %d\n", rp.getSuma());
    }

}
