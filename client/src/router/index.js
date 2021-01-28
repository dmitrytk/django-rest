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

];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
