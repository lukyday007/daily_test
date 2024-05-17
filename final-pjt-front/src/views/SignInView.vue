<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signup">
      <label for="username">username : </label>
      <input type="text" id="username" v-model.trim="username"><br>
    
      <label for="nickname">닉네임 : </label>
      <input type="text" id="nickname" v-model.trim="nickname"><br>

      <label for="email">이메일 : </label>
      <input type="text" id="email" v-model.trim="email"><br>

      <label for="password1">비밀번호 : </label>
      <input type="password" id="password1" v-model.trim="password1"><br>

      <label for="password2">비밀번호 확인 : </label>
      <input type="password" id="password2" v-model.trim="password2"><br>

      <label for="age">나이 : </label>
      <input type="text" id="age" v-model.trim="age"><br>

      <label for="salary">연봉 : </label>
      <input type="text" id="salary" v-model.trim="salary"><br>

      <label for="balance">통장 잔액 : </label>
      <input type="text" id="balance" v-model.trim="balance"><br>

      <label for="debt">대출 금액 : </label>
      <input type="text" id="debt" v-model.trim="debt"><br>

      <label for="creditscore">신용 점수 : </label>
      <input type="text" id="creditscore" v-model.trim="creditscore"><br>

      <input type="submit" value="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const username = ref(null)
const nickname = ref(null)
const email = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const age = ref(null)
const salary = ref(null)
const balance = ref(null)
const debt = ref(null)
const creditscore = ref(null)

const signup = function () {
  const payload = {
    username: username.value,
    nickname: nickname.value,
    email: email.value,
    password1: password1.value,
    password2: password2.value,
    age: age.value,
    salary: salary.value,
    balance: balance.value,
    debt: debt.value,
    creditscore: creditscore.value,
  }
  store.signUp(payload)
}
</script>

<style scoped>

</style>