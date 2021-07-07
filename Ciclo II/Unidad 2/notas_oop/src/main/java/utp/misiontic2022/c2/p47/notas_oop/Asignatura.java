package utp.misiontic2022.c2.p47.notas_oop;

public class Asignatura {

    // Atributos
    private String nombreAsignatura;
    private Nota nota1;
    private Nota nota2;
    private Nota nota3;
    private Nota nota4;
    private Nota nota5;
    private Nota notaBaja;
    private Integer promedio100;

    // Constructores
    public Asignatura () {
        /*
        this.nota1 = new Nota();
        this.nota2 = new Nota();
        this.nota3 = new Nota();
        this.nota4 = new Nota();
        this.nota5 = new Nota();
        */
        setNombreAsignatura("nombreAsignatura");
        setNota1(new Nota());
        setNota2(new Nota());
        setNota3(new Nota());
        setNota4(new Nota());
        setNota5(new Nota());
    }

    public Asignatura (String pNombreAsignatura, Integer pNota1_100,
                Integer pNota2_100, Integer pNota3_100, Integer pNota4_100,
                Integer pNota5_100) {
        setNombreAsignatura(pNombreAsignatura);
        setNota1(new Nota(pNota1_100));
        setNota2(new Nota(pNota2_100));
        setNota3(new Nota(pNota3_100));
        setNota4(new Nota(pNota4_100));
        setNota5(new Nota(pNota5_100));
    }

    // Metodos
    public void mostrarAsignatura() {
        System.out.println("------InfoAsignatura------");
        System.out.println("Nombre de la asignatura: " + getNombreAsignatura());
        nota1.mostrarNota();
        nota2.mostrarNota();
        nota3.mostrarNota();
        nota4.mostrarNota();
        nota5.mostrarNota();
    }

    public void encontrarNotaBaja() {
        setNotaBaja(nota1);
        if (nota2.getEscala100() < notaBaja.getEscala100()) {
            this.notaBaja = getNota2();
        }
        if (nota3.getEscala100() < notaBaja.getEscala100()) {
            this.notaBaja = getNota3();
        }
        if (nota4.getEscala100() < notaBaja.getEscala100()) {
            this.notaBaja = getNota4();
        }
        if (nota5.getEscala100() < notaBaja.getEscala100()) {
            this.notaBaja = getNota5();
        }
    }

    public void calcularPromedio() {
        this.encontrarNotaBaja();

        this.promedio100 = (nota1.getEscala100() + nota2.getEscala100()
                        + nota3.getEscala100() + nota4.getEscala100()
                        + nota5.getEscala100() - notaBaja.getEscala100()) / 4;
    }

    public String getNombreAsignatura() {
        return nombreAsignatura;
    }

    public void setNombreAsignatura(String nombreAsignatura) {
        this.nombreAsignatura = nombreAsignatura;
    }

    public Nota getNota1() {
        return nota1;
    }

    public void setNota1(Nota nota1) {
        this.nota1 = nota1;
    }

    public Nota getNota2() {
        return nota2;
    }

    public void setNota2(Nota nota2) {
        this.nota2 = nota2;
    }

    public Nota getNota3() {
        return nota3;
    }

    public void setNota3(Nota nota3) {
        this.nota3 = nota3;
    }

    public Nota getNota4() {
        return nota4;
    }

    public void setNota4(Nota nota4) {
        this.nota4 = nota4;
    }

    public Nota getNota5() {
        return nota5;
    }

    public void setNota5(Nota nota5) {
        this.nota5 = nota5;
    }

    public Nota getNotaBaja() {
        return notaBaja;
    }

    public void setNotaBaja(Nota notaBaja) {
        this.notaBaja = notaBaja;
    }

    
    
}

    
