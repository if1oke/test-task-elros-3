<script setup>
import { ref } from 'vue'
import HistoryItem from '@/components/History/HistoryItem.vue'

const historyItemList = ref([
  { date: '2024-01-12 12:33:20', currency: 'BTC', amount: '0,12', price: '532,22', action: 'BUY', id: 1 },
  { date: '2024-01-12 12:43:20', currency: 'BTC', amount: '0,10', price: '341,22', action: 'BUY', id: 2 },
  { date: '2024-01-12 12:56:20', currency: 'TON', amount: '42,5421', price: '241,53', action: 'BUY', id: 3 },
  { date: '2024-01-12 13:02:20', currency: 'TON', amount: '12,12', price: '143,12', action: 'SELL', id: 4 },
  { date: '2024-01-12 13:15:20', currency: 'BTC', amount: '0,003', price: '45,62', action: 'SELL', id: 5 }
])
</script>

<template>
<v-card :elevation="0">
  <v-card-title>
    История сделок
  </v-card-title>
  <v-card-text>
    <history-item v-for="item in historyItemList" :data="item" :key="item.id" />
  </v-card-text>
</v-card>
</template>

<style scoped lang="scss">

</style>
