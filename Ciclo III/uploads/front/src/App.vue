<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" app>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6"> {{ title }} </v-list-item-title>
          <v-list-item-subtitle> {{ username }} </v-list-item-subtitle>
          <v-list-item-subtitle> {{ role }} </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <Menu></Menu>
    </v-navigation-drawer>

    <v-app-bar color="white" app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>{{ title }}</v-toolbar-title>

      <v-spacer></v-spacer>

      <account-button @open-login="showLogin = true"></account-button>
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-main>
      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>

    <v-dialog v-model="showLogin" persistent max-width="400">
      <Login @login-success="showLogin = false"></Login>
    </v-dialog>
  </v-app>
</template>

<script>
import AccountButton from "./components/AccountButton.vue";
import Login from "./components/Login.vue";
import Menu from "./components/Menu.vue";

export default {
  components: {
    Menu,
    AccountButton,
    Login,
  },
  data: () => ({
    showLogin: false,
    drawer: true,
    title: "APP Example",
  }),
  computed: {
    username: () => sessionStorage.getItem("username"),
    role: () => sessionStorage.getItem("role"),
  },
};
</script>
