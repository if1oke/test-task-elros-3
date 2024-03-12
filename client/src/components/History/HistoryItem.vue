<script setup>
const props = defineProps({
  data: {
    type: Object,
    required: true
  }
})
</script>

<template>
  <div class="d-flex justify-space-between hover my-1 py-1 px-2 rounded align-center">
    <div class="fixed-width">
      {{ props.data.date }}
    </div>
    <div class="fixed-width">
      <v-chip
        size="small"
        :color="props.data.action === 'SELL' ? 'yellow' : 'green'"
      >
        {{ props.data.action }}
      </v-chip>
    </div>
    <div class="fixed-width">
      {{ props.data.currency }}
      <v-icon
        size="16"
        :color="props.data.currency === 'BTC' ? 'orange-lighten-2' : 'indigo-lighten-3'"
      >
        {{ props.data.currency === 'BTC' ? 'mdi-currency-btc' : 'mdi-diamond-stone'}}
      </v-icon>
    </div>
    <div class="fixed-width">
      {{ props.data.amount }}
    </div>
    <div class="fixed-width">
      {{ props.data.price }}
    </div>
  </div>
</template>

<style scoped lang="scss">
.fixed-width {
  min-width: 70px;
}
.hover:hover {
  background: #424242;
}
</style>
