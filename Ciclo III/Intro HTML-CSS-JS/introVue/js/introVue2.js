// Vue2

let app = new Vue({
    el: '#introVue',
    data: {
        saludo: 'Hola Tripulantes',
        anio: 2021,
        texto: '<p style="color:green; font-size:25px;">Soy un texto con estilo</p>',
        multiplicacion: 5*2,
        url: 'https://www.google.com',
        target: '_blank'
    },
    computed: {
        reverso : function() {
            return this.saludo.split('').reverse().join('')
        }
    },
    methods: {
        // get
        reversoF() {
            return this.saludo.split('').reverse().join('');
        }
    }
})


// Vue3
/*
const app = {
    data() {
        return {
            saludo: 'Hola Tripulantes',
            anio: 2021,
            texto: '<p style="color:green; font-size:25px;">Soy un texto con estilo</p>',
            multiplicacion: 5*2
        }
    },
    methods: {
        // get
        reversoF() {
            return this.saludo.split('').reverse().join('');
        }
    }
}

Vue.createApp(app).mount('#introVue')
*/