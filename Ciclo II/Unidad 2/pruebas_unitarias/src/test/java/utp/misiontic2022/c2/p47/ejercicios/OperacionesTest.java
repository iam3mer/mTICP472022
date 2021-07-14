package utp.misiontic2022.c2.p47.ejercicios;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

public class OperacionesTest {

    @Test
    @DisplayName("5 + 3 = 8")
    void sumaDosNumeros() {
        Operaciones suma = new Operaciones();
        
        assertEquals(8, suma.sumar(5, 3));
    }

    @ParameterizedTest()
    @CsvSource({
        "4.0,1.0,4",
        "3.0,2.0,8,",
        "4.0,2.0,8,"
    })
    void testMultiplicar(double num1, double num2, int result) {
        Operaciones multiplica = new Operaciones();

        assertEquals(result, multiplica.multiplicar(num1, num2),
            () -> num1 + " * " + num2 + " = " + result);

        //assertEquals(4.0, multiplica.multiplicar(4.0, 1.0));
        //assertEquals(6.0, multiplica.multiplicar(3.0, 2.0));
        //assertEquals(8.0, multiplica.multiplicar(4.0, 2.0));
    }
    
}
