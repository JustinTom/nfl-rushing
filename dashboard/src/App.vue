<template>
  <v-app>
    <v-main>
      <app-header></app-header>
      <router-view></router-view>
      <scroll-top></scroll-top>
    </v-main>
  </v-app>
</template>

<script>
import header from './components/header.vue';
import scrollToTop from './components/scrollToTop.vue';

export default {
  name: 'App',

  components: {
    'app-header': header,
    'scroll-top': scrollToTop,
  },

  data: () => ({
    //
  }),
};
</script>
