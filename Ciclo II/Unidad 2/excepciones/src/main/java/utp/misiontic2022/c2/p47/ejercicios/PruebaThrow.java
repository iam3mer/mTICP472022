package utp.misiontic2022.c2.p47.ejercicios;

public class PruebaThrow {

    private int num1;
    private int num2;

    public PruebaThrow(){}

    public PruebaThrow(int num1, int num2){
        this.num1 = num1;
        this.num2 = num2;
    }

    public void divide0(int num1, int num2) throws ArithmeticException {
        System.out.println(num1/num2);
    }
}
