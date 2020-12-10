import Vue from 'vue';
import VueRouter from 'vue-router';
import DB from '@/views/DB.vue';
import Home from '@/views/Home.vue';
import Sandbox from '@/views/Sandbox.vue';
import Import from '@/views/Import.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/db',
    name: 'DB',
    component: DB,
  },
  {
    path: '/sandbox',
    name: 'Sandbox',
    component: Sandbox,
  },
  {
    path: '/import',
    name: 'Import',
    component: Import,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
