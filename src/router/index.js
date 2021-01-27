import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Homepage.vue'
import Dashboard from '../views/Dashboard.vue'
import Building from '../views/dashboard/Building.vue'
import Region from '../views/dashboard/Region.vue'
import NotFoundPage from '../views/NotFound.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/dashboard',
    component: Dashboard,
    redirect: '/dashboard/region',
    children: [
      {
      path: 'region',
      component: Region
    },
    {
      path: 'building',
      component: Building
    }
  ]
  },
  {
    path: '*', component: NotFoundPage
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router