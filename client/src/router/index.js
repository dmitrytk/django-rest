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
            component: () => import(/* webpackChunkName: "main-import" */ '../views/Import.vue'),
          },
          {
            path: 'db',
            component: () => import(/* webpackChunkName: "main-db" */ '../views/Database.vue'),
            children: [
              {
                path: 'wells',
                component: () => import(/* webpackChunkName: "main-db-wells" */ '../views/db/Wells.vue'),
              },
            ],
          },
          {
            path: 'tools/calculator',
            component: () => import(/* webpackChunkName: "main-tools-calculator" */ '../views/tools/Calculator.vue'),
          },
          {
            path: 'tools/sql',
            component: () => import(/* webpackChunkName: "main-tools-sql" */ '../views/tools/SQLGenerator.vue'),
          },
          {
            path: 'tools/converter',
            component: () => import(/* webpackChunkName: "main-tools-converter" */ '../views/tools/CoordinateConverter.vue'),
          },
          {
            path: 'tools/decline',
            component: () => import(/* webpackChunkName: "main-tools-decline" */ '../views/tools/Decline.vue'),
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
