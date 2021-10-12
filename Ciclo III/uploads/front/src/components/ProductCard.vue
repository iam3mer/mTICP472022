<template>
  <v-card>
    <v-img
      :src="imageUrl"
    ></v-img>
    <v-card-title>{{ item.name }}</v-card-title>
    <v-card-subtitle><b>Price:</b> {{ item.price }}</v-card-subtitle>
    <div class="categories">
      <v-chip v-for="category in item.categories" :key="category">{{
        category
      }}</v-chip>
    </div>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="success" :to="'/products/' + item.code"> Editar </v-btn>
      <v-btn color="error" @click="eliminar()"> Eliminar </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { deleteProduct } from "../controllers/Product.controller";

export default {
  props: ["item"],
  methods: {
    editar() {
      this.$router.push(`/products/${this.item.code}`);
    },
    eliminar() {
      deleteProduct(this.item.code)
        .then(() => {
          window.location.reload();
        })
        .catch((err) => console.error(err.response.data.message));
    },
  },
  computed: {
    imageUrl() {
      return this.item.imageUrl == undefined
        ? "https://isocarp.org/app/uploads/2014/05/noimage.jpg"
        : this.item.imageUrl;
    },
  },
};
</script>

<style scope>
.categories {
  display: flex;
  padding: 10px;
  justify-content: center !important;
  gap: 10px;
}
</style>