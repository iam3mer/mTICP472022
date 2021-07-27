package utp.misiontic2022.c2.p47.unidad4;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class WritePeople {

    public static void write() {
        String nomFile = "people.data";

        try {
            FileOutputStream file = new FileOutputStream(nomFile);
            ObjectOutputStream oos = new ObjectOutputStream(file);
            
            oos.writeObject(new People("Andres", "Barbosa", "Bogota", 20));
            oos.writeObject(new People("Carlos", "¨Figueroa", "Manizales", 21));
            oos.writeObject(new People("Nelsi", "Miramag", "Barranquilla", 20));
            oos.writeObject(new People("Andres", "Garcia", "Manizales", 22));

            oos.close();
        } catch (IOException e) {
            System.err.println(e);
        }
    }
}
