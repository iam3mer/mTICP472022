package utp.misiontic2022.c2.p47.unidad4;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.List;

public class WritePeople {

    public static void write(String nomFile, List<People> people) {
        //String nomFile = "people.data";

        try {
            FileOutputStream file = new FileOutputStream(nomFile);
            ObjectOutputStream oos = new ObjectOutputStream(file);
            
            for (People person : people) {
                oos.writeObject(person);
            }

            oos.close();
        } catch (IOException e) {
            System.err.println(e);
        }
    }
}
