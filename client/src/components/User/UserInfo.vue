<script setup>
import { mainStore } from '@/store/mainStore'

const store = mainStore()

</script>

<template>
<div class="d-flex">
  <div class="pa-1">
    <v-avatar color="primary">
      <h2>
        {{ store.user.username?.substring(0,2) }}
      </h2>
    </v-avatar>
  </div>
  <div class="d-flex flex-column align-start">
    <h4>{{ store.user.username }}</h4>
    <span>{{ store.user.email }}</span>
  </div>
</div>
</template>

<style scoped lang="scss">

</style>
