<script setup>

import BalanceChip from '@/components/Balance/BalanceChip.vue'
import { mainStore } from '@/store/mainStore'

const store = mainStore()
</script>

<template>
  <balance-chip
    :balance="store.user.wallet.ton.value"
    :tooltip="store.user.wallet.ton.address"
    color="indigo-lighten-3"
    icon="mdi-diamond-stone"
    class="me-2"
  />
  <balance-chip
    :balance="store.user.wallet.btc.value"
    :tooltip="store.user.wallet.btc.address"
    color="orange-lighten-2"
    icon="mdi-currency-btc"
    class="me-2"
  />
  <balance-chip
    :balance="store.user.wallet.usd.value"
    class="me-2" />
</template>

<style scoped lang="scss">

</style>
