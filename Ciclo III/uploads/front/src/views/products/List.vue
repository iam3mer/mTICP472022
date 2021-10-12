<template>
  <div class="products">
    <h1>Product List</h1>
    <v-btn color="primary" to="/products/new">New product</v-btn>
    <v-container>
      <v-row>
        <v-col
          v-for="product in products"
          :key="product.code"
          md="4"
          sm="6"
          cols="12"
        >
          <ProductCard :item="product"></ProductCard>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { getAllProducts } from "../../controllers/Product.controller";
import ProductCard from "../../components/ProductCard.vue";

export default {
  components: {
    ProductCard,
  },
  data() {
    return {
      products: [],
    };
  },
  created() {
    getAllProducts()
      .then((response) => {
          this.products = response.data;
      })
      .catch((err) => console.error(err.response.data.message));
  },
};
</script>

<style>
</style>