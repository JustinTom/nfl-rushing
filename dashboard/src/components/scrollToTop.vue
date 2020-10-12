<template>
  <v-btn id='topBtn' fab dark small v-on:click='scrollToTop'>
    <v-icon dark>
      mdi-chevron-up
    </v-icon>
  </v-btn>
</template>

<script>
export default {
  methods: {
    scrollToTop() {
      window.scroll({
        top: 0,
        behavior: 'smooth',
      });
    },
  },
};

window.onscroll = function () {
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    document.getElementById('topBtn').style.display = 'block';
  } else {
    document.getElementById('topBtn').style.display = 'none';
  }
};
</script>

<style>
  #topBtn {
    display: none;
    position: fixed;
    bottom: 5vmin;
    right: 2vmin;
    z-index: 99;
    border: none;
    outline: none;
    background-color: #ffbf01;
    cursor: pointer;
    opacity: 0.7;
  }

  #topBtn:hover {
    background-color: #555;
    text-decoration: none;
  }
</style>
