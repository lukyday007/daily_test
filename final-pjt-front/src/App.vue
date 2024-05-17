<template>
  <header>
    <div>
      <nav>
        <RouterLink to="/">Main</RouterLink> |

        <RouterLink :to="{name:'login'}">로그인</RouterLink> |
        <RouterLink :to="{name:'signin'}">회원가입</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>


<style scoped>
</style>
