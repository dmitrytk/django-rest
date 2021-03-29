import Vue from 'vue';
import WellService from '../../service/well.service';
import FieldService from '../../service/field.service';

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
      cases: null,
      perforations: null,
      pumps: null,
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
    setCases(state, payload) {
      state.cases = payload;
    },
    setPerforations(state, payload) {
      state.perforations = payload;
    },
    setPumps(state, payload) {
      state.pumps = payload;
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
    async deleteWell(context, id) {
      return WellService.delete(id);
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
      context.dispatch('fetchCases', id);
      context.dispatch('fetchPerforations', id);
      context.dispatch('fetchPumps', id);
    },

    // GET CHILD OBJECTS
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
    async fetchCases({ commit }, id) {
      const res = await WellService.getCases(id);
      commit('setCases', res.data);
    },
    async fetchPerforations({ commit }, id) {
      const res = await WellService.getPerforations(id);
      commit('setPerforations', res.data);
    },
    async fetchPumps({ commit }, id) {
      const res = await WellService.getPumps(id);
      commit('setPumps', res.data);
    },

    // DELETE CHILD OBJECTS
    async deleteInclinometry(context, id) {
      await WellService.deleteInclinometry(id);
    },
    async deleteMer(context, id) {
      await WellService.deleteMer(id);
    },
    async deleteRates(context, id) {
      await WellService.deleteRates(id);
    },
    async deleteZones(context, id) {
      await WellService.deleteZones(id);
    },
    async deleteCases(context, id) {
      await WellService.deleteCases(id);
    },
    async deletePerforations(context, id) {
      await WellService.deletePerforations(id);
    },
    async deletePumps(context, id) {
      await WellService.deletePumps(id);
    },

    async updateWell(context, data) {
      try {
        const well = await WellService.update(data.id, data);
        await context.dispatch('fetchWell', well.data.id);
        await context.dispatch('fetchWells', well.data.field);
        Vue.toasted.show('Сохранено');
      } catch (err) {
        Vue.toasted.show('Ошибка');
        console.log(err);
      }
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
    cases: (state) => state.cases,
    perforations: (state) => state.perforations,
    pumps: (state) => state.pumps,

  },
};
