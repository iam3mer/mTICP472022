package utp.misiontic2022.c2.p47.unidad4;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class ReadPeople {
    public static void read() {
        String nomFile = "people.data";

        try {
            FileInputStream file = new FileInputStream(nomFile);
            ObjectInputStream ois = new ObjectInputStream(file);

            var p1 = (People) ois.readObject();

            System.out.println(p1.toString());

            ois.close();
        } catch (IOException e) {
            System.err.println(e);
        } catch (ClassNotFoundException e) {
            System.err.println(e);
        }
    }
}
