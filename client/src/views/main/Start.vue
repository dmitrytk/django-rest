<template>
  <router-view></router-view>
</template>

<script>
import store from '@/store';

const startRouteGuard = async (to, from, next) => {
  await store.dispatch('auth/checkLoggedIn');
  if (store.getters['auth/isLoggedIn']) {
    if (to.path === '/login' || to.path === '/') {
      next('/main');
    } else {
      next();
    }
  } else if (store.getters['auth/isLoggedIn'] === false) {
    if (to.path === '/' || (to.path).startsWith('/main')) {
      next('/login');
    } else {
      next();
    }
  }
};

export default {
  name: 'Start',

  beforeRouteEnter(to, from, next) {
    startRouteGuard(to, from, next);
  },

  beforeRouteUpdate(to, from, next) {
    startRouteGuard(to, from, next);
  },
};
</script>
