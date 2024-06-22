import { createRouter, createWebHistory } from 'vue-router'
import MenuPage from '../components/pages/MenuPage.vue'
import GraphPage from '../components/pages/GraphPage.vue'
import AboutPage from '../components/pages/AboutPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/filter',
      name: 'menu-filter',
      component: MenuPage
    },
    {
      path: '/graphs',
      name: 'graph-display',
      component: GraphPage
    },
    {
      path: '/about',
      name: 'aboutPage',
      component: AboutPage
    },
    
  ]
})

export default router
