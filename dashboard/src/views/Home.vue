<template>
  <div>
    <app-header></app-header>
    <h1 class="text-center">NFL Rushing</h1>

    <v-divider></v-divider>

    <dataTable></dataTable>
  </div>
</template>

<script>
import dataTable from '../components/dataTable.vue';
import header from '../components/header.vue';

export default {
  name: 'Home',
  components: {
    dataTable,
    'app-header': header,
  },
};
</script>
