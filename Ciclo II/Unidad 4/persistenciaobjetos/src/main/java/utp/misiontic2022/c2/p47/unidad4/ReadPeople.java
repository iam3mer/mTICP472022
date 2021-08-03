package utp.misiontic2022.c2.p47.unidad4;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class ReadPeople {
    
    private static Integer suma = 0;

    public ReadPeople(){};

    public void read() {
        String nomFile = "people.data";

        try (
            FileInputStream file = new FileInputStream(nomFile);
            ObjectInputStream ois = new ObjectInputStream(file);
        ) {
        
            People person = (People) ois.readObject();

            while (person != null) {

                if (person instanceof People) {
                    //System.out.println(person.toString());
                    System.out.println(person);

                    setSuma(getSuma() + person.getAge());
                    //this.suma = this.suma + person.getAge();
                }
                
                person = (People) ois.readObject();
            }
        } catch (EOFException e) {
        } catch (IOException e) {
            System.err.println(e);
        } catch (ClassNotFoundException e) {
            System.err.println(e);
        } 
    }

    public Integer getSuma() {
        return suma;
    }

    public void setSuma(Integer suma) {
        this.suma = suma;
    }

    
}
