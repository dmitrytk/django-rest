import Vue from 'vue';
import Vuex from 'vuex';
import fields from './fields.module';
import load from './load.module';
import wells from './wells.module';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    fields,
    load,
    wells,
  },
});
