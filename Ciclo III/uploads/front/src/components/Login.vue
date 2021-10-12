<template>
  <v-card>
    <v-card-title>Autenticación</v-card-title>
    <v-card-text>
      <v-text-field
        v-model="username"
        :rules="rulesUsername"
        label="Usuario"
        prepend-icon="mdi-account-circle"
      ></v-text-field>

      <v-text-field
        v-model="password"
        :rules="rulesPassword"
        :type="showPassword ? 'text' : 'password'"
        label="Contraseña"
        prepend-icon="mdi-lock"
        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        @click:append="showPassword = !showPassword"
      ></v-text-field>
      <v-alert border="left" color="red lighten-2" dark v-model="showError">
        {{ error }}
      </v-alert>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="info" @click="login()">Ingresar</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { validateUser } from "../controllers/Login.controller";

export default {
  data() {
    return {
      showPassword: false,
      username: "",
      password: "",
      rulesUsername: [
        (value) => !!value || "Requerido.",
        (value) => value && value.length <= 50,
      ],
      rulesPassword: [
        (value) => !!value || "Requerido.",
        (value) => value && value.length <= 50,
      ],
      showError: false,
      error: "",
    };
  },
  methods: {
    login() {
      validateUser(this.username, this.password)
        .then((response) => {
          const user = response.data;
          sessionStorage.setItem("username", user.username);
          sessionStorage.setItem("role", user.role);
          this.$emit("login-success", this.username);
          window.location.reload();
        })
        .catch((err) => {
          this.showError = true;
          this.error = err.response.data.message;
          setInterval(() => {
            this.showError = false;
          }, 3000);
        });
    },
  },
};
</script>

<style>
</style>