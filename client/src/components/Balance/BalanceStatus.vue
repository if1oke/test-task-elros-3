<script setup>

import { ref } from 'vue'
import BalanceChip from '@/components/Balance/BalanceChip.vue'

const balance = ref({
  usd: '112,99',
  btc: '0,5672',
  ton: '62,122'
})
</script>

<template>
  <balance-chip :balance="balance.ton" color="indigo-lighten-3" icon="mdi-diamond-stone" class="me-2" />
  <balance-chip :balance="balance.btc" color="orange-lighten-2" icon="mdi-currency-btc" class="me-2" />
  <balance-chip :balance="balance.usd" class="me-2" />
</template>

<style scoped lang="scss">

</style>
