<template>
  <v-card>
    <v-btn
      elevation="2"
      @click="guardar"
    >Guardar</v-btn>
    <v-alert
      type="success"
      v-if="mensaje"
    >
    {{ mensaje }}
    </v-alert>
    <v-card-title>
      Nutrition
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="desserts"
      :search="search"
    ></v-data-table>
  </v-card>
</template>

<script>
  import { getAllBooks, insertBook } from "../../services/BooksService";

  export default {
    name: 'Table',
    data () {
      return {
        search: '',
        headers: [
          {
            text: 'ISBN',
            align: 'start',
            value: 'isbn',
          },
          { text: 'Titulo', value: 'title' },
          { text: 'Autores', value: 'autores' },
          { text: 'Descripcion', value: 'descripcion' },
          { text: 'Portada', value: 'portada' },
        ],
        desserts: [],
      }
    },
    mounted () {
      getAllBooks()
        .then((response) => {
          this.desserts = response.data;
        })
        .catch((err) => console.error(err));
    },
    methods: {
      guardar () {
        const book = {
          isbn: "sdfgsdfdfgd",
          title: "Nuevo Libro",
          autores: ["el autor"],
          descripcion: "sdfsdkfshd fshdf sdkfhs dfkshfk shdfks",
          portada: "https://images.cdn2.buscalibre.com/fit-in/360x360/ae/b5/aeb5d6a9452b04aec0aafeb7a22e120f.jpg"
        }
        insertBook(book)
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
