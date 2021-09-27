<template>
  <v-card>
      <v-card-title>
          {{ infoService.title }}
      </v-card-title>

      <v-card-text>
          {{ infoService.text }}
      </v-card-text>
  </v-card>
</template>

<script>
export default {
    name: 'Service',
    props: [
        'infoService',
    ]

}
</script>

<style>

</style>