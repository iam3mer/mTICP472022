/*
let elemento = document.getElementById('title-header');
elemento.style.color="#0000FF";
elemento.style.backgroundColor="#00FF00";

let elementos = document.getElementsByClassName('card');
// console.log(elementos);
elementos[0].style.backgroundColor="#0F0";

elementos = document.getElementsByTagName('li');
// console.log(elementos);
elementos[1].style.color="#F00";

elemento = document.querySelector('#title-header');
// console.log(elemento);
elemento.style.color="white";
elemento.style.backgroundColor="initial";

elemento = document.querySelector('.list-group-item');
// console.log(elemento);
elemento.style.fontSize='20px';

elementos = document.querySelectorAll('.list-group-item');
console.log(elementos);
*/

const itemsArray = [];

window.onload = () => {
    const form = document.getElementById('inputForm');
    
    form.onsubmit = (e) => {

        e.preventDefault();
        const item = document.getElementById('item');
        const txtItem = item.value;
        console.log(txtItem);

        itemsArray.push(txtItem);

        for (let)
        
        const itemList = document.getElementById('items');

        itemList.innerHTML = `<li>${txtItem}</li>`;
    }
}