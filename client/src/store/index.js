import Vue from 'vue';
import Vuex from 'vuex';
import fields from './modules/fields';
import load from './modules/load';
import wells from './modules/wells';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    fields,
    load,
    wells,
  },
});
