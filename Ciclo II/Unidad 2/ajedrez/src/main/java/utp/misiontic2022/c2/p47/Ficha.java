package utp.misiontic2022.c2.p47;

public abstract class Ficha {

    // Atributos
    private Color color;

    private Casilla casilla;

    public Ficha(Color color) {
        this.color = color;
    }

    // Metodos
    public abstract Boolean comer();
    public abstract Boolean mover();

    public Casilla getCasilla() {
        return casilla;
    }

    public void setCasilla(Casilla casilla) {
        this.casilla = casilla;
    }


}
