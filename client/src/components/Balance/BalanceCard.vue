<script setup>

import BalanceStatus from '@/components/Balance/BalanceStatus.vue'
import { mainStore } from '@/store/mainStore'
import { onMounted } from 'vue'

const store = mainStore()

onMounted(async () => {
  if (store.user.authState) {
    await store.getWallet()
  }
})
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
