// Comentarios de una linea

/*
* Comentarios de multiples lineas
*/

// Declaracón de variables
// var
// let
// const

// Tipos de Datos
// Numeric
// String
// Boolean
// Objetos

let numero = 10;
numero = 20.0;

let cadenas = "Hola Tripulantes";
cadenas = 'Esta es otra cadena';
cadenas = '4';

let boleano = true;
boleano = false;

let objeto = {nombre:"Jhonatan", apellido:"Barrera"};

// Matrices
let array = ["Pereira", "Manizales", "Armenia"];

//concat()
//indexOf()
//lastIndexOf()
//join()
//pop()
//push()
//shift()
//unshift()
//reverse()
//slice()
//sort()
//toString()
//length()
//valueOf()

//Operadores
// +
// - 
// /
// *
// %
// ++
// --
// ()

// Operadores de comparacion
// <
// <=
// >=
// >
// ?
// ==
// ===
// !=
// !==

// Operadores Logicos
// and &&
// or ||
// not !

// Funciones
function name(params1, params2) {
    //code
}

let miFuncion = (a,b) => a+b;
let miFuncion2 = (a,b) => {
    a += 5;
    return b + a;
}

// Salida de datos
//console.log()
//alert()
//confirm()
//prompt()

// Ciclos
// for
for (let i=0; i<5; i++) {
    document.write(i);
}
// while
let i = 0;
let loop = true;
while (loop) {
    console.log(i);
    i++;
    if (i == 4) {
        loop = false;
        //break;
    }
}

//Date
Date()