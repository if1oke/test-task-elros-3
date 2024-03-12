<script setup>
const props = defineProps({
  balance: {
    type: String,
    required: true
  },
  color: {
    type: String,
    required: false,
    default: 'green-lighten-2'
  },
  icon: {
    type: String,
    required: false,
    default: 'mdi-currency-usd'
  }
})
</script>

<template>
  <div>
    <v-chip :color="props.color">
      <v-icon start>
        {{ props.icon }}
      </v-icon>
      <span class="font-weight-bold text-subtitle-1">
      {{ props.balance }}
    </span>
    </v-chip>
  </div>
</template>

<style scoped lang="scss">

</style>
