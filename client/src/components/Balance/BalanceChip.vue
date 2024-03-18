<script setup>
defineProps({
  balance: {
    type: String,
    required: true
  },
  tooltip: {
    type: String,
    required: false,
    default: 'Доллары США'
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
    <v-tooltip :text="tooltip" location="bottom">
      <template v-slot:activator="{ props }">
        <v-chip v-bind="props" :color="color">
          <v-icon start>
            {{ icon }}
          </v-icon>
          <span class="font-weight-bold text-subtitle-1">
        {{ balance }}
      </span>
        </v-chip>
      </template>
    </v-tooltip>
  </div>
</template>

<style scoped lang="scss">

</style>
