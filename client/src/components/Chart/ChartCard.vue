<script setup>
import { mainStore } from '@/store/mainStore'
import { onMounted } from 'vue'
import ChartItem from '@/components/Chart/ChartItem.vue'

const store = mainStore()

onMounted(async () => {
  await store.getExchangeHistory()
  setInterval(async () => {
    await store.getExchangeHistory()
  }, 60 * 1000)
})
</script>

<template>
<v-card :elevation="0">
  <v-card-title>
    График стоимости валют
  </v-card-title>
  <v-card-text class="d-flex flex-column">
    <v-row>
      <v-col cols="12" md="6">
        <chart-item name="Bitcoin" currency="btc" />
      </v-col>
      <v-col cols="12" md="6">
        <chart-item name="TON" currency="ton" />
      </v-col>
    </v-row>
  </v-card-text>
</v-card>
</template>

<style scoped lang="scss">

</style>
