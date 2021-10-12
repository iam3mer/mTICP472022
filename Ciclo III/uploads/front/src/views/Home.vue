<template>
  <div class="home">
    <h1>This is an home page</h1>
    <v-list>
      <v-subheader>REPORTS</v-subheader>
      <v-list-item-group v-model="selectedItem" color="primary">
        <v-list-item v-for="(item, i) in items" :key="i">
          <v-list-item-icon>
            <v-img max-height="24" max-width="24" :src="item.image"></v-img>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.name"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedItem: 1,
      items: [
        { name: "Dato 1", image: require("../assets/img/imagen1.png") },
        { name: "Dato 2", image: require("../assets/img/imagen2.png") },
        { name: "Dato 3", image: require("../assets/img/imagen3.png") },
        { name: "Dato 4", image: require("../assets/img/imagen4.png") },
      ],
    };
  },
};
</script>
