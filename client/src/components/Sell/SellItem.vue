<script setup>
const props = defineProps({
  data: {
    type: Object,
    required: true
  }
})
</script>

<template>
<div class="d-flex flex-row justify-space-between my-1 hover py-1 px-2 rounded align-center">
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
    <v-icon>
      mdi-equal
    </v-icon>
  </div>
  <div class="fixed-width">
    {{ props.data.price }} $
  </div>
  <div class="fixed-width">
    <v-btn
      size="small"
      color="yellow"
      :elevation="0"
    >
      Продать
    </v-btn>
  </div>
</div>
</template>

<style scoped lang="scss">
.hover:hover {
  background: #424242;
}
.fixed-width {
  min-width: 50px;
}
</style>
