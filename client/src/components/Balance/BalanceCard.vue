<script setup>

import BalanceStatus from '@/components/Balance/BalanceStatus.vue'
</script>

<template>
  <v-card :elevation="0">
    <v-card-title>
      Ваш кошелек
    </v-card-title>
    <v-card-text class="d-flex">
      <balance-status />
    </v-card-text>
  </v-card>
</template>

<style scoped lang="scss">

</style>
