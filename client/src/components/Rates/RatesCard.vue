<script setup>
import { ref } from 'vue'
import RatesItem from '@/components/Rates/RatesItem.vue'

const exchangeRates = ref([
  {
    currency: 'BTC',
    rate: '61231,44',
    color: 'orange-lighten-2',
    icon: 'mdi-currency-btc'
  },
  {
    currency: 'TON',
    rate: '3,66',
    color: 'indigo-lighten-3',
    icon: 'mdi-diamond-stone'
  }
])
</script>

<template>
<v-card :elevation="0">
  <v-card-title>
    Текущий курс
  </v-card-title>
  <v-card-text class="d-flex">
    <rates-item
      v-for="(item, idx) in exchangeRates"
      :key="idx"
      :exchange-rate="item.rate"
      :color="item.color"
      :icon="item.icon"
      :currency="item.currency"
      class="mx-2"
    />
  </v-card-text>
</v-card>
</template>

<style scoped lang="scss">

</style>
