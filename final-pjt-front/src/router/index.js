import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import SignInView from '@/views/SignInView.vue'
import LoginView from '@/views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path:'/login',
      name: 'login',
      component: LoginView,
    },
    {
      path:'/signin',
      name: 'signin',
      component: SignInView,
    }
  ]
})

export default router
