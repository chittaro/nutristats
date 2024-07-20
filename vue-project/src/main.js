import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap-slider/dist/css/bootstrap-slider.min.css';
import 'bootstrap-slider/dist/bootstrap-slider.min.js';

import './assets/reset.css'
import './assets/style.css'
  
const app = createApp(App)

app.use(router)
app.mount('#app')