import { createRouter, createWebHistory } from 'vue-router'
import MenuPage from '../components/pages/MenuPage.vue'
import PlannerPage from '../components/pages/PlannerPage.vue'
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
      path: '/planner',
      name: 'plannerPage',
      component: PlannerPage
    },
    {
      path: '/about',
      name: 'aboutPage',
      component: AboutPage
    },
    
  ]
})

export default router
