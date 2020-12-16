import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import * as GmapVue from 'gmap-vue';
import App from './App.vue';
import router from './router';
import store from './store';
import './scss/custom.scss';
import './scss/style.scss';

// Install BootstrapVue
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

Vue.config.productionTip = false;

Vue.use(GmapVue, {
  load: {
    key: process.env.VUE_APP_MAP_API_KEY,
  },
  installComponents: true,
});
new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
