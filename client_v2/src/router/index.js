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
