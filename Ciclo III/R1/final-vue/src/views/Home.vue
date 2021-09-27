<template>
  <div>
    <Carrousel />

    <div class="d-flex flex-wrap justify-space-between mb-2">
      <div class="pa-2" v-for="(service, index) in 3" :key="service">
        <Service :infoService=infoService[index] />
      </div>
    </div>

    <v-row no-gutters>
      <template v-for="n, i in 4">
        <v-col class="pa-2" :key="n">
          <!-- <v-card
            class="pa-2"
            outlined
            tile
          > -->
            <Note :infoNote=infoNote[i] />
          <!-- </v-card> -->
        </v-col>
        <v-responsive
          v-if="n === 2"
          :key="`width-${n}`"
          width="100%"
        ></v-responsive>
      </template>
    </v-row>

  </div>
</template>

<script>
import Carrousel from '../components/Carrousel.vue'
import Note from '../components/Note.vue'
import Service from '../components/Service.vue'

  export default {
    name: 'Home',
    data: () => ({
      infoService: [
        {
          title: 'Servicio 1',
          text: 'dsfgdfgdfgdfgdfgdfgdfgdfgdfgdfggbjkhfgvkhfjhgfdjhgfhgfjhgfjhgfj'
        },{
          title: 'Servicio 2',
          text: 'dsfgdfgdfgdfgdfgdfgdfgdfgdfgdfggbjkhfgvkhfjhgfdjhgfhgfjhgfjhgfj'
        },{
          title: 'Servicio 3',
          text: 'dsfgdfgdfgdfgdfgdfgdfgdfgdfgdfggbjkhfgvkhfjhgfdjhgfhgfjhgfjhgfj'
        },{
          title: 'Servicio 4',
          text: 'dsfgdfgdfgdfgdfgdfgdfgdfgdfgdfggbjkhfgvkhfjhgfdjhgfhgfjhgfjhgfj'
        },{
          title: 'Servicio 5',
          text: 'dsfgdfgdfgdfgdfgdfgdfgdfgdfgdfggbjkhfgvkhfjhgfdjhgfhgfjhgfjhgfj'
        },
      ],
      infoNote: [
        {
          title: 'Titulo de la nota 1',
          abstract: 'Resumen de la nota',
          text: 'dfgdfgdfgdfgdfgdfgdfgdfgdfg'
        },
        {
          title: 'Titulo de la nota 2',
          abstract: 'Resumen de la nota',
          text: 'dfgdfgdfgdfgdfgdfgdfgdfgdfg'
        },
        {
          title: 'Titulo de la nota 3',
          abstract: 'Resumen de la nota',
          text: 'dfgdfgdfgdfgdfgdfgdfgdfgdfg'
        },
        {
          title: 'Titulo de la nota 4',
          abstract: 'Resumen de la nota',
          text: 'dfgdfgdfgdfgdfgdfgdfgdfgdfg'
        },
        {
          title: 'Titulo de la nota 5',
          abstract: 'Resumen de la nota',
          text: 'dfgdfgdfgdfgdfgdfgdfgdfgdfg'
        },
        {
          title: 'Titulo de la nota 6',
          abstract: 'Resumen de la nota',
          text: 'dfgdfgdfgdfgdfgdfgdfgdfgdfg'
        },
      ],
    }),
    components: {
      Carrousel,
        Service,
        Note,
    },
  }
</script>
