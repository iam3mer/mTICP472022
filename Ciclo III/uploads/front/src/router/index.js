import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routeGuard = (to, from, next) => {
  let isAuthenticated = false;
  if (sessionStorage.getItem("username")) {
    isAuthenticated = true;
  }

  if (isAuthenticated) {
    next();
  } else {
    next("/");
  }
};

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/products',
    name: 'Products',
    component: () => import('../views/products/List.vue'),
    beforeEnter: routeGuard
  },
  {
    path: '/products/new',
    name: 'New Product',
    component: () => import('../views/products/New.vue'),
    beforeEnter: routeGuard
  },
  {
    path: '/products/:code',
    name: 'Edit Product',
    component: () => import('../views/products/New.vue'),
    beforeEnter: routeGuard
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
