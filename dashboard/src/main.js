import Vue from 'vue';
import JsonExcel from 'vue-json-excel';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false;

Vue.component('downloadExcel', JsonExcel);

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
