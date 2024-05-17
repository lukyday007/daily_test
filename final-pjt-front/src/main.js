import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useKakao } from 'vue3-kakao-maps/@utils'
import App from './App.vue'
import router from './router'

const app = createApp(App)

useKakao('f17d3b983009a990f4c003735aac44b6', ['clusterer', 'services', 'drawing']);

app.use(createPinia())
app.use(router)

app.mount('#app')
