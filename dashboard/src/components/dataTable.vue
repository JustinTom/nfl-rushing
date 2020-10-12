<template>
  <v-card>
    <v-card-title>
      <!-- Search field -->
      <v-text-field
        v-model='search'
        append-icon='mdi-magnify'
        label='Player Search'
        type='text'
      ></v-text-field>

      <v-spacer></v-spacer>

      <!-- Download button exporting the filtered data to a CSV file -->
      <download-excel
        :data='filteredPlayers'
        type='csv'
        name='playerData.csv'
        :escapeCsv=false
        :before-generate='startDownload'
        :before-finish='cleanUpDownload'
      >
        <v-btn
          color='#0078fd'
          fab
          :loading='downloadBtnLoadingFlag'
          :disabled='downloadBtnLoadingFlag'
        >
        <v-icon>mdi-download</v-icon>
      </v-btn>
      </download-excel>
    </v-card-title>

    <v-data-table
      :headers='headers'
      :items='players'
      :search='search'
      :footer-props="{
        'items-per-page-options': [25, 50, 75, 100, -1]
      }"
      ref='statsTable'
      class='elevation-1'
      loading=true
      no-results-text='No results found.'
      no-data-text="No data retrieved."
    >

      <!-- Tool tip clarity on header names. -->
      <template v-for='h in headers' v-slot:[`header.${h.value}`]='{ header }'>
        <v-tooltip bottom v-bind:key='h.id'>
          <template v-slot:activator="{ on }">
            <span v-on="on">{{header.text}}</span>
          </template>
          <span>{{header.tooltip}}</span>
        </v-tooltip>
      </template>

      <!-- Anchor links for each player's NFL profile. -->
      <template v-slot:item.Player='{ item }'>
        <a v-bind:href='generateNFLPlayerURL(item.Player)' target='_blank'>{{ item.Player }}</a>
      </template>

      <!-- Visual rating indicators for certain stat categories. -->
      <template v-slot:item.Yds='{ item }'>
        <v-chip :color='getRatingColor(item.Yds, totalRushingYardsMax)'> {{ item.Yds }}</v-chip>
      </template>
      <template v-slot:item.Lng='{ item }'>
        <v-chip :color='getRatingColor(item.Lng, longestRushMax)'> {{ item.Lng }}</v-chip>
      </template>
      <template v-slot:item.TD='{ item }'>
        <v-chip :color='getRatingColor(item.TD, totalRushingTouchdownsMax)'> {{ item.TD }}</v-chip>
      </template>

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
          tooltip: 'Player\'s name',
        },
        {
          text: 'Team',
          filterable: false,
          value: 'Team',
          tooltip: 'Player\'s team abbreviation',
        },
        {
          text: 'Position',
          filterable: false,
          value: 'Pos',
          tooltip: 'Player\'s position',
        },
        {
          text: 'Att',
          filterable: false,
          value: 'Att',
          tooltip: 'Rushing attempts',
        },
        {
          text: 'Avg Att',
          filterable: false,
          value: 'Att/G',
          tooltip: 'Rushing attempts per game average',
        },
        {
          text: 'Yds',
          filterable: false,
          value: 'Yds',
          tooltip: 'Total rushing yards',
        },
        {
          text: 'Avg Yds',
          filterable: false,
          value: 'Avg',
          tooltip: 'Rushing average yards per attempt',
        },
        {
          text: 'Yds/G',
          filterable: false,
          value: 'Yds/G',
          tooltip: 'Rushing yards per game',
        },
        {
          text: 'TD',
          filterable: false,
          value: 'TD',
          tooltip: 'Total rushing touchdowns',
        },
        {
          text: 'Lng',
          filterable: false,
          value: 'Lng',
          tooltip: 'Longest rush (a \'T\' represents a touchdown occured)',
        },
        {
          text: 'Rush 1st',
          filterable: false,
          value: '1st',
          tooltip: 'Rushing first downs',
        },
        {
          text: 'Rush 1st%',
          filterable: false,
          value: '1st%',
          tooltip: 'Rushing first down percentage',
        },
        {
          text: '20+',
          filterable: false,
          value: '20+',
          tooltip: 'Rushing 20+ yards each',
        },
        {
          text: '40+',
          filterable: false,
          value: '40+',
          tooltip: 'Rushing 40+ yards each',
        },
        {
          text: 'Rush FUM',
          filterable: false,
          value: 'FUM',
          tooltip: 'Rushing fumbles',
        },
      ],
      players: [],
      filteredPlayers: [],
      search: '',
      downloadBtnLoadingFlag: false,
    };
  },
  created() {
    axios
      .get('http://localhost:8001/players')
      .then((response) => { this.players = response.data; });
  },
  beforeUpdate() {
    this.totalRushingYardsMax = this.getHighestStatValue(this.players, 'Yds');
    this.longestRushMax = this.getHighestStatValue(this.players, 'Lng');
    this.totalRushingTouchdownsMax = this.getHighestStatValue(this.players, 'TD');
  },
  methods: {
    startDownload() {
      this.downloadBtnLoadingFlag = true;
      this.filteredPlayers = this.$refs.statsTable.$children[0].filteredItems;
    },
    cleanUpDownload() {
      this.downloadBtnLoadingFlag = false;
    },
    generateNFLPlayerURL(name) {
      return `https://nfl.com/players/${name.toLowerCase().replaceAll(' ', '-')}`;
    },
    sanitizeLongestRushValue(lngValue) {
      if (typeof lngValue === 'string' && lngValue.includes('T')) {
        // In the case of longest rush, convert it to an int and
        // add 10 yards to compensate for a touchdown.
        return Number(lngValue.toString().replace('T', '')) + 10;
      }
      return lngValue;
    },
    // Calculate and set the max values for stats.
    getHighestStatValue(playerData, stat) {
      // Create a deep copy of the array in order to manipulate outlier values
      // such as Lng's 'touchdown' strings. Since simply assigning 'playerData'
      // to another variable makes it reference the same object in memory.
      const sanitizedPlayerData = JSON.parse(JSON.stringify(playerData));

      if (stat === 'Lng') {
        Object.keys(sanitizedPlayerData).forEach((player) => {
          Object.keys(sanitizedPlayerData[player]).forEach((playerStat) => {
            if (playerStat === 'Lng') {
              sanitizedPlayerData[player][playerStat] = this.sanitizeLongestRushValue(
                playerData[player][playerStat],
              );
            }
          });
        });
      }

      return Math.max(...sanitizedPlayerData.map((player) => player[stat]), 0);
    },
    getRatingColor(currValue, highestValue) {
      const sanitizedValue = this.sanitizeLongestRushValue(currValue);
      const score = sanitizedValue / highestValue;

      if (score < 0.25) {
        return 'red';
      }
      if (score < 0.5) {
        return 'orange';
      }
      if (score < 0.75) {
        return 'amber';
      }
      return 'green';
    },
  },
};
</script>

<style>
  table thead tr{
    background: black;
  }
</style>
