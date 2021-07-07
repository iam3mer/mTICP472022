package utp.misiontic2022.c2.p47.notas_oop;

public class Nota {
    
    // Atributos
    private Integer escala100;
    private Double escala5;
    private String escalaCualitativa;

    // Constructores
    Nota() {
        this.escala100 = 0;
        this.escala5 = 0.0;
        this.escalaCualitativa = "";
    }

    Nota(Double pEscala5) {
        setEscala100(Integer.parseInt(Double.toString(pEscala5)) * 20);
        setEscala5(pEscala5);
        if (pEscala5 >= 3.0){
            setEscalaCualitativa("Aprobado");
        } else {
            setEscalaCualitativa("Reprobado");
        }
    }

    Nota(Integer pEscala100) {
        setEscala100(pEscala100);
        setEscala5(pEscala100 * 0.05);
        if (pEscala100 >= 60){
            setEscalaCualitativa("Aprobado");
        } else {
            setEscalaCualitativa("Reprobado");
        }
    }

    // Metodos
    public void mostrarNota() {
        System.out.println("------EscalaNota------");
        System.out.printf("Nota en escala 100: %d\n", this.escala100);
        System.out.printf("Nota en escala 5: %.2f\n", getEscala5());
        System.out.printf("Nota en escala cualitativa: %s\n", this.escalaCualitativa);
    }

    public Double getEscala5() {
        return escala5;
    }

    public void setEscala5(Double escala5) {
        this.escala5 = escala5;
    }

    public Integer getEscala100() {
        return escala100;
    }

    public void setEscala100(Integer escala100) {
        this.escala100 = escala100;
    }

    public String getEscalaCualitativa() {
        return escalaCualitativa;
    }

    public void setEscalaCualitativa(String escalaCualitativa) {
        this.escalaCualitativa = escalaCualitativa;
    }

    

}
