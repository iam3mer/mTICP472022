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

const itemsArray = JSON.parse(localStorage.getItem('itemsArray')) || [];

const ls = () => {
    const itemsString = JSON.stringify(itemsArray)
    localStorage.setItem('itemsArray', itemsString)
}

const render = () => {
    const itemsList = document.getElementById('items');

    itemsList.innerHTML = '';
    for (let i=0; i<itemsArray.length; i++) {
        itemsList.innerHTML += `<li>${itemsArray[i]}</li>`;
    }

    const elementos = document.querySelectorAll('#items li');
    elementos.forEach((elemento, i) => {
        
        elemento.classList.add('list-group-item');

        elemento.addEventListener('click', () => {

            elemento.parentNode.removeChild(elemento);
            itemsArray.splice(i,1)

            //localstorage
            ls();

            render();
        })
    })
}

window.onload = () => {

    render();

    const form = document.getElementById('inputForm');
    
    form.onsubmit = (e) => {

        e.preventDefault();
        const item = document.getElementById('item');
        const txtItem = item.value;
        item.value = '';
        if (txtItem != ''){
            itemsArray.push(txtItem);
        }

        //localstorage
        ls();
        
        render();
    }
}