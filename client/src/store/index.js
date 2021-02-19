import Vue from 'vue';
import Vuex from 'vuex';
import fields from './modules/fields.module';
import load from './modules/load.module';
import wells from './modules/wells.module';
import auth from './modules/auth.module';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    fields,
    load,
    wells,
    auth,
  },
});
