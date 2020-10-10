<template>
  <v-app>
    <v-main>
      <app-header></app-header>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import header from './components/header.vue';

export default {
  name: 'App',

  components: {
    'app-header': header,
  },

  data: () => ({
    //
  }),
};
</script>
