import { createRouter, createWebHistory } from 'vue-router'
import DashView from '@/views/DashView.vue'

const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: DashView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
