<template>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
</template>

<script>
import Navbar from '@/component/Navbar.vue';

export default {
  name: 'App',
  components: {
    Navbar,
  },
};
</script>
