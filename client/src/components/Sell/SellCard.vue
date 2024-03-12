<script setup>
import SellItem from '@/components/Sell/SellItem.vue'

const sellItemsList = [
  { currency: 'TON', amount: '2,433', id: 1, description: 'Blah blah', price: '29,99' },
  { currency: 'TON', amount: '1,511', id: 2, description: 'Blah blah', price: '19,99' },
  { currency: 'TON', amount: '3,356', id: 3, description: 'Blah blah', price: '39,99' },
  { currency: 'BTC', amount: '0,0023', id: 4, description: 'Blah blah', price: '39,99' },
  { currency: 'BTC', amount: '0,0049', id: 5, description: 'Blah blah', price: '69,99' }
]
</script>

<template>
<v-card width="450" class="mx-2" :elevation="0">
  <v-card-title>
    Запросы продажи
  </v-card-title>
  <v-card-text>
    <sell-item v-for="item in sellItemsList" :data="item" :key="item.id" />
  </v-card-text>
</v-card>
</template>

<style scoped lang="scss">

</style>
