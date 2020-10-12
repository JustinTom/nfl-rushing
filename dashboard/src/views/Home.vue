<template>
  <div>
    <app-header></app-header>

    <h1 class="text-center my-5">NFL Rushing</h1>

    <v-divider></v-divider>

    <data-table></data-table>
  </div>
</template>

<script>
import dataTable from '@/components/dataTable.vue';
import header from '@/components/header.vue';

export default {
  name: 'Home',
  components: {
    'data-table': dataTable,
    'app-header': header,
  },
};
</script>
