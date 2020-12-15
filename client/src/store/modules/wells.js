import WellService from '../../service/WellService';
import FieldService from '../../service/FieldService';

export default {
  namespaced: true,
  state: () => (
    {
      well: null,
      wells: null,
      wellLoading: false,
      wellsLoading: false,
      inclinometry: null,
      mer: null,
      rates: null,
      zones: null,
    }
  ),
  mutations: {
    setWellsLoading(state, IsLoading) {
      state.wellsLoading = IsLoading;
    },
    setWellLoading(state, IsLoading) {
      state.wellLoading = IsLoading;
    },
    setWell(state, payload) {
      state.well = payload;
    },
    setWells(state, payload) {
      state.wells = payload;
    },
    setInclinometry(state, payload) {
      state.inclinometry = payload;
    },
    setMer(state, payload) {
      state.mer = payload;
    },
    setRates(state, payload) {
      state.rates = payload;
    },
    setZones(state, payload) {
      state.zones = payload;
    },
  },
  actions: {
    async fetchWell(context, id) {
      context.commit('setWellLoading', true);
      const well = await WellService.findOne(id);
      context.dispatch('fetchWellData', id);
      context.commit('setWell', well.data);
      context.commit('setWellLoading', false);
    },
    async fetchWells({ commit }, fieldId) {
      commit('setWellsLoading', true);
      const wells = await FieldService.getWells(fieldId);
      commit('setWells', wells.data);
      commit('setWellsLoading', false);
    },
    async fetchWellData(context, id) {
      context.dispatch('fetchInclinometry', id);
      context.dispatch('fetchMer', id);
      context.dispatch('fetchRates', id);
      context.dispatch('fetchZones', id);
    },
    async fetchInclinometry({ commit }, id) {
      const res = await WellService.getInclinometry(id);
      commit('setInclinometry', res.data);
    },
    async fetchMer({ commit }, id) {
      const res = await WellService.getMer(id);
      commit('setMer', res.data);
    },
    async fetchRates({ commit }, id) {
      const res = await WellService.getRates(id);
      commit('setRates', res.data);
    },
    async fetchZones({ commit }, id) {
      const res = await WellService.getZones(id);
      commit('setZones', res.data);
    },
    async updateWell(context, data) {
      const well = await WellService.update(data.id, data);
      context.commit('setWell', well.data);
      context.commit('setWellLoading', false);
      await context.dispatch('fetchWells', well.data.field);
    },
  },
  getters: {
    well: (state) => state.well,
    wells: (state) => state.wells,
    wellLoading: (state) => state.wellLoading,
    wellsLoading: (state) => state.wellsLoading,
    inclinometry: (state) => state.inclinometry,
    mer: (state) => state.mer,
    rates: (state) => state.rates,
    zones: (state) => state.zones,

  },
};
