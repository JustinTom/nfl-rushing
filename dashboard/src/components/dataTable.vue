<template>
  <v-card>
    <v-data-table
      :headers='headers'
      :items='players'
      :footer-props="{
        'items-per-page-options': [25, 50, 75, 100, -1]
      }"
      class='elevation-1'
      loading=true
      no-results-text='No results found.'
      no-data-text="No data retrieved."
    >
    </v-data-table>
  </v-card>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      headers: [
        {
          text: 'Name',
          value: 'Player',
        },
        {
          text: 'Team',
          filterable: false,
          value: 'Team',
        },
        {
          text: 'Position',
          filterable: false,
          value: 'Pos',
        },
        {
          text: 'Att',
          filterable: false,
          value: 'Att',
        },
        {
          text: 'Avg Att',
          filterable: false,
          value: 'Att/G',
        },
        {
          text: 'Yds',
          filterable: false,
          value: 'Yds',
        },
        {
          text: 'Avg Yds',
          filterable: false,
          value: 'Avg',
        },
        {
          text: 'Yds/G',
          filterable: false,
          value: 'Yds/G',
        },
        {
          text: 'TD',
          filterable: false,
          value: 'TD',
        },
        {
          text: 'Lng',
          filterable: false,
          value: 'Lng',
        },
        {
          text: 'Rush 1st',
          filterable: false,
          value: '1st',
        },
        {
          text: 'Rush 1st%',
          filterable: false,
          value: '1st%',
        },
        {
          text: '20+',
          filterable: false,
          value: '20+',
        },
        {
          text: '40+',
          filterable: false,
          value: '40+',
        },
        {
          text: 'Rush FUM',
          filterable: false,
          value: 'FUM',
        },
      ],
      players: [],
    };
  },
  created() {
    axios
      .get('http://localhost:8001/players')
      .then((response) => { this.players = response.data; });
  },
  methods: {
  },
};
</script>

<style>
  table thead tr{
    background: black;
  }
</style>
