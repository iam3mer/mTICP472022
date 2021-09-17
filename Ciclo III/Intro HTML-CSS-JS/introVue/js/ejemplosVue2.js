let Contador = new Vue({
    el: '#contador',
    data: {
        cont: 0
    },
    mounted() {
        setInterval(() => {
            this.cont++
        }, 1000);
    }
})

let Reverso = new Vue({
    el: '#reverso',
    data: {
        mensaje: 'Estamos probando Vue',
        stilo: 'btn btn-secondary mb-2 col-3'
    },
    methods: {
        reverso() {
            this.mensaje = this.mensaje.split('').reverse().join('')
        },
        stilo() {
            this.mensaje = '********************'
        }
    }
})