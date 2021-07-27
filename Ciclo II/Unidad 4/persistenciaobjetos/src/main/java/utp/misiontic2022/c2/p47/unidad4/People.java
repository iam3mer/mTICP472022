package utp.misiontic2022.c2.p47.unidad4;

import java.io.Serializable;

public class People implements Serializable {
    private String first_name;
    private String last_name;
    private String city;
    private Integer age;

    public People(String first_name, String last_name, String city, Integer age) {
        this.first_name = first_name;
        this.last_name = last_name;
        this.city = city;
        this.age = age;
    }

    @Override
    public String toString() {
        return getFirst_name()+" "+getLast_name()+": "+getAge();
    }

    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }

    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    
}
