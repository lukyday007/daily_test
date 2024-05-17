<template>
  <header>
    <div>
      <nav>
        <RouterLink to="/">Main</RouterLink> |
        <RouterLink :to="{name:'map'}">Map</RouterLink> |
        <RouterLink v-if="!store.isLogin" :to="{name:'login'}">로그인</RouterLink> |
        <button v-if="store.isLogin" @click="store.logOut">로그아웃</button>
        <RouterLink v-if="!store.isLogin" :to="{name:'signin'}">회원가입</RouterLink>
      </nav>


    </div>
  </header>
  <RouterView />
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useUserStore } from '@/stores/user'
const store = useUserStore()

</script>


<style scoped>
</style>
