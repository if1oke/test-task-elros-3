<script setup>
import BuyItem from '@/components/Buy/BuyItem.vue'

const buyItemsList = [
  { currency: 'TON', amount: '3,12', id: 1, description: 'Blah blah', price: '8,99' },
  { currency: 'BTC', amount: '0,1', id: 2, description: 'Blah blah', price: '600' },
  { currency: 'TON', amount: '3,356', id: 3, description: 'Blah blah', price: '39,99' },
  { currency: 'TON', amount: '0,0023', id: 4, description: 'Blah blah', price: '42,33' },
  { currency: 'BTC', amount: '0,0015', id: 5, description: 'Blah blah', price: '24,99' }
]
</script>

<template>
<v-card width="450" class="mx-2" :elevation="0">
  <v-card-title>
    Предложения покупки
  </v-card-title>
  <v-card-text>
    <buy-item v-for="item in buyItemsList" :key="item.id" :data="item" />
  </v-card-text>
</v-card>
</template>

<style scoped lang="scss">

</style>
