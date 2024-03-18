<template>
<v-app>
  <v-layout>
    <app-bar />
    <v-main
      class="d-flex justify-space-around mt-5"
    >
      <router-view />
    </v-main>
  </v-layout>
</v-app>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.content {
  min-width: 800px !important;
}
</style>
<script setup>
import AppBar from '@/components/common/AppBar.vue'
</script>
