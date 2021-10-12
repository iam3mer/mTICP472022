<template>
  <div class="new-product">
    <h1>{{ isNew ? "New" : "Edit" }} Product</h1>
    <div v-if="!changeImage">
      <v-img v-if="!isNew" :src="imageUrl"></v-img>
      <v-file-input
        v-if="isNew"
        accept="image/*"
        label="Image"
        v-model="image"
        :rules="imageRules"
      ></v-file-input>
      <v-text-field
        label="Code"
        v-model="code"
        prepend-icon="mdi-code-tags"
      ></v-text-field>
      <v-text-field
        label="Name"
        v-model="name"
        prepend-icon="mdi-account"
      ></v-text-field>
      <v-text-field
        label="Price"
        v-model="price"
        prepend-icon="mdi-currency-usd"
      ></v-text-field>
      <v-combobox
        prepend-icon="mdi-shape"
        v-model="categories"
        chips
        clearable
        label="Categories"
        multiple
        solo
      >
        <template v-slot:selection="{ attrs, item, select, selected }">
          <v-chip
            v-bind="attrs"
            :input-value="selected"
            close
            @click="select"
            @click:close="removeChip(item)"
          >
            {{ item }}
          </v-chip>
        </template>
      </v-combobox>

      <div class="botones">
        <v-btn color="primary" @click="guardarProducto()" v-if="isNew"
          >Guardar</v-btn
        >
        <v-btn color="warning" @click="changeImage = true" v-if="!isNew"
          >Actualizar imagen</v-btn
        >
        <v-btn color="success" @click="actualizarProducto()" v-if="!isNew"
          >Actualizar</v-btn
        >
      </div>
    </div>
    <div v-if="changeImage">
      <v-file-input
        accept="image/*"
        label="Image"
        v-model="image"
        :rules="imageRules"
      ></v-file-input>
      <div class="botones">
        <v-btn color="success" @click="cambiarImagen()"
          >Actualizar imagen</v-btn
        >
      </div>
    </div>

    <v-snackbar v-model="snackbar">
      {{ snackbarText }}

      <template v-slot:action="{ attrs }">
        <v-btn color="pink" text v-bind="attrs" @click="closeConfirmation()">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
import {
  createProduct,
  createProductWithImage,
  getProduct,
  updateProduct,
  updateProductImage,
} from "../../controllers/Product.controller";

export default {
  data() {
    return {
      image: null,
      code: 0,
      name: "",
      price: 0,
      categories: [],
      imageUrl: "",
      snackbar: false,
      snackbarText: "",
      isNew: true,
      imageRules: [
        (value) =>
          !value ||
          value.size < 2000000 ||
          "Avatar size should be less than 2 MB!",
      ],
      changeImage: false,
    };
  },
  created() {
    const code = this.$route.params.code;
    if (code != undefined) {
      getProduct(code)
        .then((response) => {
          const product = response.data;
          this.code = product.code;
          this.name = product.name;
          this.price = product.price;
          this.categories = product.categories;
          this.imageUrl = product.imageUrl;

          this.isNew = false;
        })
        .catch((err) => console.error(err));
    }
  },
  methods: {
    guardarProducto() {
      let request = null;
      if (this.image == null || this.image == undefined) {
        const product = {
          code: this.code,
          name: this.name,
          price: this.price,
          categories: this.categories,
        };

        request = createProduct(product);
      } else {
        const product = new FormData();
        product.append("code", this.code);
        product.append("name", this.name);
        product.append("price", this.price);
        product.append("categories", JSON.stringify(this.categories));
        product.append("image", this.image);

        request = createProductWithImage(product);
      }

      request
        .then(() => {
          this.openSuccessDialog("Guardado correctamente");
        })
        .catch((err) => console.error(err));
    },
    actualizarProducto() {
      if (
        this.code == undefined ||
        this.code == "" ||
        this.name == undefined ||
        this.name == "" ||
        this.price == undefined ||
        this.price == ""
      ) {
        this.openErrorDialog("Ingrese los campos obligatorios");
        return;
      }

      const product = {
        code: this.code,
        name: this.name,
        price: this.price,
        categories: this.categories,
      };
      updateProduct(this.code, product)
        .then(() => {
          this.changeImage = false;
          this.openSuccessDialog("Se ha actualizado el producto: " + this.code);
        })
        .catch(() => this.openErrorDialog("Error al actualizar el producto"));
    },
    cambiarImagen() {
      if (this.image == undefined || this.image == "") {
        this.openErrorDialog("La imagen es un campo obligatorio");
        return;
      }

      const data = new FormData();
      data.append("image", this.image);
      updateProductImage(this.code, data)
        .then(() =>
          this.openSuccessDialog("Se ha actualizado el producto: " + this.code)
        )
        .catch(() => this.openErrorDialog("Error al actualizar el producto"));
    },
    removeChip(item) {
      this.categories.splice(this.categories.indexOf(item), 1);
      this.categories = [...this.categories];
    },
    openSuccessDialog(mensaje) {
      this.snackbarText = mensaje;
      this.snackbar = true;
    },
    openErrorDialog(mensaje) {
      this.snackbarText = mensaje;
      this.snackbar = true;
    },
    closeConfirmation() {
      this.snackbar = false;
      this.$router.push("/products");
    },
  },
};
</script>

<style scope>
.botones {
  display: flex;
  justify-content: right;
}
</style>