<script setup>
const props = defineProps({
  exchangeRate: {
    type: String,
    required: true
  },
  color: {
    type: String,
    required: false,
    default: 'green'
  },
  icon: {
    type: String,
    required: false,
    default: 'mdi-currency-usd'
  },
  currency: {
    type: String,
    required: false,
    default: 'USD'
  }
})
</script>

<template>
<div>
  <v-chip
    :color="props.color"
    :prepend-icon="props.icon"
  >
    <v-icon class="me-2">
      mdi-equal
    </v-icon>
    <span class="font-weight-bold text-subtitle-1">
      {{ props.exchangeRate }} $
    </span>
  </v-chip>
</div>
</template>

<style scoped lang="scss">

</style>
