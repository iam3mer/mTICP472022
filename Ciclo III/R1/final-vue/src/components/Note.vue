<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-card-title>
        {{ infoNote.title }}
    </v-card-title>
    <v-card-text>
        {{ infoNote.abstract }}
    </v-card-text>

    <v-card-actions>
      <v-btn
        text
        color="teal accent-4"
        @click="reveal = true"
      >
        Leer noticia completa >>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <v-card
        v-if="reveal"
        class="transition-fast-in-fast-out v-card--reveal"
        style="height: 100%;"
      >
        <v-card-text class="pb-0">
          <p class="text-h4 text--primary">
            {{ infoNote.title }}
          </p>
          <p> {{ infoNote.text }} </p>
        </v-card-text>
        <v-card-actions class="pt-0">
          <v-btn
            text
            color="teal accent-4"
            @click="reveal = false"
          >
            Cerrar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-expand-transition>
  </v-card>
</template>

<script>
  export default {
    name: 'Note',
    data: () => ({
      reveal: false,
    }),
    props: [
        'infoNote',
    ]
  }
</script>

<style>
.v-card--reveal {
  bottom: 0;
  opacity: 1 !important;
  position: absolute;
  width: 100%;
}
</style>