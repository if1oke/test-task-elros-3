<script setup>

import { mainStore } from '@/store/mainStore'
import { onMounted, ref } from 'vue'

defineProps(['name', 'currency'])

const store = mainStore()
const ready = ref(false)

onMounted(() => {
  ready.value = true
})

</script>

<template>
<v-card class="mx-auto overflow-visible" :elevation="0">
  <v-sheet
    class="mx-auto"
    color=""
    :elevation="0"
    rounded="lg"
  >
    <v-sparkline
      :labels="store.exchange.history[currency].map(item => `$ ${item}`)"
      :model-value="store.exchange.history[currency]"
      :color="currency === 'btc' ? 'orange-lighten-2' : 'indigo-lighten-3'"
      line-width="2"
      :smooth="true"
      padding="16"
    ></v-sparkline>
  </v-sheet>
</v-card>
</template>

<style scoped lang="scss">

</style>
