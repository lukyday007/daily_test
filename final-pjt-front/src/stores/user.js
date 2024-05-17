import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        console.log('로그인 성공!')
        token.value = response.data.key
        router.push({ name : 'main' })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2, nickname, email, age, salary, balance, debt, creditscore } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname, email, age, salary, balance, debt, creditscore
      }
    })
     .then((response) => {
       console.log('회원가입 성공!')
       const password = password1
       logIn({ username, password })
     })
     .catch((error) => {
       console.log(error)
     })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      headers: { Authorization: `Token ${token.value}`}
    })
      .then(res => {
        console.log(res.data)
        token.value = null  // token 초기화
        router.push({ name: 'login' })
      })
      .catch(err => {
        console.log(err)
      })
  }

  return { token, logIn, signUp, logOut, isLogin }
})
