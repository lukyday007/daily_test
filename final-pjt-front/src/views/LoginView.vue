<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <div>
        <label for="username">username : </label>
        <input type="text" v-model.trim="username" id="username">
      </div>
      <div>
        <label for="password">password : </label>
        <input type="password" v-model.trim="password" id="password">
      </div>
      <input type="submit">
    </form>
  </div>

  <div>
    <br>
    <span>아직 회원이 아니라면 => </span>
    <RouterLink :to="{name:'signin'}">회원가입</RouterLink>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'

const username = ref(null)
const password = ref(null)
const store = useUserStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>

<style>

</style>
