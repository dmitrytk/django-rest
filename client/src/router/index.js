import Vue from 'vue';
import VueRouter from 'vue-router';
import DB from '@/views/DB.vue';
import Home from '@/views/Home.vue';
import Sandbox from '@/views/Sandbox.vue';
import Import from '@/views/Import.vue';
import Wells from '@/views/db/Wells.vue';
import Map from '@/views/db/Map.vue';
import FieldData from '@/views/db/FieldData.vue';
import SQLGenerator from '@/views/SQLGenerator.vue';
import CoordinateConverter from '@/views/CoordinateConverter.vue';
import WaterCalculator from '@/views/WaterCalculator.vue';
import Decline from '@/views/Decline.vue';
import Login from '@/views/Login.vue';
import { USER_KEY } from '../common/config';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/db/',
    name: 'DB',
    component: DB,
    children: [
      {
        path: 'wells',
        name: 'Wells',
        component: Wells,
      },
      {
        path: 'map',
        name: 'Map',
        component: Map,
      },
      {
        path: 'field',
        name: 'field',
        component: FieldData,
      },
    ],
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
  {
    path: '/decline',
    name: 'Decline',
    component: Decline,
  },
  {
    path: '/sql',
    name: 'SQLGenerator',
    component: SQLGenerator,
  },
  {
    path: '/converter',
    name: 'CoordinateConverter',
    component: CoordinateConverter,
  },
  {
    path: '/calculator',
    name: 'WaterCalculator',
    component: WaterCalculator,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  { path: '*', redirect: '/' },

];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

// eslint-disable-next-line consistent-return
router.beforeEach((to, from, next) => {
  const publicPages = ['/login', '/'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem(USER_KEY);

  if (authRequired && !loggedIn) {
    return next('/login');
  }

  next();
});

export default router;
