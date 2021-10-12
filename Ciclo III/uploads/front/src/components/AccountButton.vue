<template>
  <v-menu left bottom>
    <template v-slot:activator="{ on, attrs }">
      <v-btn icon v-bind="attrs" v-on="on">
        <v-icon>mdi-account</v-icon>
      </v-btn>
    </template>

    <v-list>
      <v-list-item v-if="!isLoggedIn" link @click="openLogin()">
        <v-list-item-title>Iniciar sesión</v-list-item-title>
      </v-list-item>
      <v-list-item v-if="isLoggedIn" link>
        <v-list-item-title>Perfil</v-list-item-title>
      </v-list-item>
      <v-list-item v-if="isLoggedIn" link @click="logOut()">
        <v-list-item-title>Cerrar sesión</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    openLogin() {
      console.log("Abrir login");
      this.$emit("open-login", null);
    },
    logOut() {
        sessionStorage.removeItem("username");
        sessionStorage.removeItem("role");
        window.location.reload();
    },
  },
  computed: {
    isLoggedIn() {
      return sessionStorage.getItem("username") != undefined;
    },
  },
};
</script>

<style>
</style>