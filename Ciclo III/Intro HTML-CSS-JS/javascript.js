function incrementar() {
    const txt = document.getElementById("inputBox");
    txt.value = parseInt(txt.value) + 1;
    console.log(txt.value);
}

function mostrarCaracter() {
    const cadena = document.getElementById("input2").value;
    const parrafo = document.getElementById("mostrar");

    parrafo.innerHTML = `<strong>${cadena}</strong>`;
}