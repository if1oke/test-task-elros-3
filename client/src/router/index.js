import { createRouter, createWebHistory } from 'vue-router'
import DashView from '@/views/DashView.vue'
import AuthView from '@/views/AuthView.vue'
import { mainStore } from '@/store/mainStore'
import { LSGetToken } from '@/utils'

const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: DashView
  },
  {
    path: '/auth',
    name: 'auth',
    component: AuthView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, from, next) => {
  const store = mainStore()
  if (to.name === 'auth') {
    next()
    return
  }
  if (store.user.authState) {
    next()
    return
  }

  const { access } = LSGetToken()
  if (access) {
    try {
      console.log('get user profile (router)')
      await store.getProfile()
      next()
    } catch (e) {
      console.error(e)
      next({ name: 'auth' })
    }
  } else {
    next({ name: 'auth' })
  }
})

export default router
