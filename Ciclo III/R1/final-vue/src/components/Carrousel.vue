<template>
  <v-carousel hide-delimiters>
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
      :src="item.src"
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
  export default {
    name: 'Carrousel',
    data () {
      return {
      }
    },
    props: [
        'items',
    ]
  }
</script>

<style>

</style>