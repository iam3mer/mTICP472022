package utp.misiontic2022.c2.p47;

public class Casilla {

    private final Color color;
    private final Integer columna;
    private final Integer fila;

    private Ficha ficha;

    public Casilla(Integer fila, Integer columna) {
        this.fila = fila;
        this.columna = columna;

        this.color = (fila + columna) % 2 == 0 ? Color.BLANCO : Color.NEGRO;
    }

    public boolean ocupada() {
        return ficha != null;
    }

    public void ubicarFicha(Ficha ficha) {
        this.ficha = ficha;
        this.ficha.setCasilla(this);
    }

    public Ficha obtenerFicha(){
        return ficha;
    }

    public void retirarFicha() {
        this.ficha = null;
    }
    
}
