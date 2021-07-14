package utp.misiontic2022.c2.p47.ejercicios;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        //listas();
        //conjuntos();
        mapas();
    }

    public static void listas(){

        System.out.println("-------------Lista de Objetos-----------");

        MiObjeto demo = new MiObjeto();

        List<Object> lista = new ArrayList<>();

        lista.add(7);
        lista.add(9);
        lista.add(1, 4.0);
        lista.add(demo);

        lista.remove(4.0);
        lista.get(lista.indexOf(9));

        for (int i = 0; i < lista.size(); i++) {
            System.out.println(lista.get(i));
        }

        // Foreach
        for (Object objeto: lista) {
            System.out.println(objeto);
        }

        Iterator<Object> iterador = lista.iterator();
        while(iterador.hasNext()){
            Object objeto = iterador.next();
            System.out.println(objeto);
        }

        List<Integer> listaEnteros = new ArrayList<>();

        listaEnteros.add(45);
        listaEnteros.add(34);
        listaEnteros.add(36);
        listaEnteros.add(786);

        listaEnteros.forEach((entero) -> {
            Integer auxEntero = entero * 2;
            System.out.println(auxEntero);
        }
            );

    }

    public static void conjuntos(){

        var conjunto = new HashSet<Integer>();

        conjunto.add(7);
        conjunto.add(34);
        conjunto.add(34);
        conjunto.add(563);

        for (Integer entero: conjunto){
            System.out.println(entero);
        }

        var conjuntoL = new LinkedHashSet<>();

        conjuntoL.add(7);
        conjuntoL.add(34);
        conjuntoL.add(34);
        conjuntoL.add(563);

        conjuntoL.remove(34);

        System.out.println(conjuntoL);

        System.out.println("Tamaño del conjunto: "+conjunto.size());
    }

    public static void mapas(){

        Map<String, Object> mapa = new LinkedHashMap<>();

        mapa.put("key", "value");
        mapa.put("Asignatura", "Programación");
        mapa.put("Nota", 2.5);
        mapa.put("Tripulante", "Francisco");

        System.out.println(mapa);

        System.out.println(mapa.containsKey("Nota"));
        System.out.println(mapa.containsValue(5.0));

        mapa.remove("key");
        System.out.println(mapa);

        mapa.put("Nota", 3.0);

        System.out.println(mapa.keySet());

        Set<String> llaves = mapa.keySet();
        for (String llave : llaves) {
            System.out.println(mapa.get(llave));
        }

    }
}
