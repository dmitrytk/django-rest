import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    field: null,
    wells: null,
    well: null,
  },
  mutations: {
    setField(state, payload) {
      state.field = payload;
    },
    setWells(state, payload) {
      state.wells = payload;
    },
    setWell(state, payload) {
      state.well = payload;
    },
  },
  actions: {},
  modules: {},
});
