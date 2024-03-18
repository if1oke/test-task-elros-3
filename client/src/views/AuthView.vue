<script setup>
import { ref } from 'vue'
import { mainStore } from '@/store/mainStore'
import { useRouter } from 'vue-router'

const store = mainStore()
const router = useRouter()

const login = ref()
const password = ref()
const email = ref()

const showRegister = ref(false)

const processRegister = async () => {
  try {
    await store.doRegister(
      login.value,
      email.value,
      password.value
    )
    await toMainPage()
  } catch (e) {
    console.error(e)
  }
}

const processLogin = async () => {
  try {
    await store.doAuth(
      login.value,
      password.value
    )
    await toMainPage()
  } catch (e) {
    console.error(e)
  }
}

const toMainPage = async () => {
  await router.push({ name: 'dashboard' })
}
</script>

<template>
<div class="login-form">
  <v-text-field
    placeholder="Логин"
    v-model="login"
    variant="solo"
  />
  <v-text-field
    placeholder="Пароль"
    v-model="password"
    type="password"
    variant="solo"
  />
  <div class="d-flex justify-space-between">
    <v-btn
      variant="outlined"
      color="primary"
      @click="showRegister = true"
    >
      Регистрация
    </v-btn>
    <v-btn
      color="primary"
      @click="processLogin"
    >
      Войти
    </v-btn>
  </div>
</div>
<v-dialog v-model="showRegister" width="500">
  <v-card>
    <v-card-text>
      <v-text-field
        v-model="login"
        variant="solo"
        placeholder="Логин"
      />
      <v-text-field
        v-model="email"
        variant="solo"
        placeholder="Email"
      />
      <v-text-field
        v-model="password"
        variant="solo"
        placeholder="Пароль"
      />
    </v-card-text>
    <v-card-actions class="d-flex justify-space-between">
      <v-btn
        color="black"
        variant="text"
        @click="showRegister = false"
      >
        Отмена
      </v-btn>
      <v-btn
        variant="flat"
        color="primary"
        @click="processRegister"
      >
        Зарегистрироваться
      </v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>
</template>

<style scoped lang="scss">
.login-form {
  width: 400px;
}
</style>
