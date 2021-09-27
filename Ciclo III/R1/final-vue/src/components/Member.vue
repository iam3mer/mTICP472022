<template>
  <v-card>

      <v-avatar>
      <img
        src=infoTeam.img
      >
      </v-avatar>

      <v-card-title>
          {{ infoTeam.member }}
      </v-card-title>

      <v-card-text>
          {{ infoTeam.description }}
      </v-card-text>
  </v-card>
</template>

<script>
export default {
    name: 'Member',
    props: [
        'infoTeam',
    ]

}
</script>