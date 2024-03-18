<script setup>
import { onMounted } from 'vue'
import RatesItem from '@/components/Rates/RatesItem.vue'
import { mainStore } from '@/store/mainStore'

const store = mainStore()

onMounted(async () => {
  await store.getExchangeRate()
})

</script>

<template>
<v-card :elevation="0">
  <v-card-title>
    Текущий курс
  </v-card-title>
  <v-card-text class="d-flex">
    <rates-item
      :exchange-rate="store.exchange.current.btc.rate"
      :color="store.exchange.current.btc.color"
      :icon="store.exchange.current.btc.icon"
      :currency="store.exchange.current.btc.currency"
      class="mx-2"
    />
    <rates-item
      :exchange-rate="store.exchange.current.ton.rate"
      :color="store.exchange.current.ton.color"
      :icon="store.exchange.current.ton.icon"
      :currency="store.exchange.current.ton.currency"
      class="mx-2"
    />
  </v-card-text>
</v-card>
</template>

<style scoped lang="scss">

</style>
