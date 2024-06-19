import { createApp } from 'vue'
import App from './App.vue'
import VueClickaway from "vue3-click-away"
import router from './router'

import './assets/reset.css'
import './assets/style.css'


const app = createApp(App)

app.use(router)
app.use(VueClickaway)
app.mount('#app')
