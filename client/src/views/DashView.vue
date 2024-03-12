<script setup>

import BuyCard from '@/components/Buy/BuyCard.vue'
import SellCard from '@/components/Sell/SellCard.vue'
import HistoryCard from '@/components/History/HistoryCard.vue'
import RatesCard from '@/components/Rates/RatesCard.vue'
import BalanceCard from '@/components/Balance/BalanceCard.vue'
</script>

<template>
<div class="d-flex flex-column">
  <div class="d-flex px-2 justify-space-between">
    <rates-card />
    <balance-card />
  </div>
  <div class="d-flex mt-4">
    <buy-card />
    <sell-card />
  </div>
  <div class="px-2">
    <history-card class="mt-4" />
  </div>
</div>
</template>

<style scoped lang="scss">

</style>
