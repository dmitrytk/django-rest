import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: () => import(/* webpackChunkName: "start" */ '../views/main/Start.vue'),
    children: [
      {
        path: 'main',
        component: () => import(/* webpackChunkName: "main" */ '../views/main/Main.vue'),
        children: [
          {
            path: 'dashboard',
            component: () => import(/* webpackChunkName: "main-dashboard" */ '../views/main/Dashboard.vue'),
          },
          {
            path: 'import',
            component: () => import(/* webpackChunkName: "main-dashboard" */ '../views/Import.vue'),
          },
          {
            path: 'db',
            component: () => import(/* webpackChunkName: "main-dashboard" */ '../views/Database.vue'),
          },
          {
            path: 'tools/calculator',
            component: () => import(/* webpackChunkName: "main-dashboard" */ '../views/tools/Calculator.vue'),
          },
          {
            path: 'tools/sql',
            component: () => import(/* webpackChunkName: "main-dashboard" */ '../views/tools/SQLGenerator.vue'),
          },
          {
            path: 'tools/converter',
            component: () => import(/* webpackChunkName: "main-dashboard" */ '../views/tools/CoordinateConverter.vue'),
          },
        ],
      },
    ],
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
