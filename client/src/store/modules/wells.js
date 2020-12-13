import WellService from '@/service/FieldService';

export default {
  namespaced: true,
  state: () => (
    {
      well: null,
      wells: null,
      wellLoading: false,
      wellsLoading: false,
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
  },
  actions: {
    async fetchWell({ commit }, id) {
      commit('setWellLoading', true);
      const well = await WellService.findOne(id);
      commit('setWell', well.data);
      commit('setWellLoading', false);
    },
    async fetchWells({ commit }) {
      commit('setWellsLoading', true);
      const wells = await WellService.findAll();
      commit('setWells', wells.data);
      commit('setWellsLoading', false);
    },
  },
  getters: {
    well: (state) => state.well,
    wells: (state) => state.wells,
    wellLoading: (state) => state.wellLoading,
    wellsLoading: (state) => state.wellsLoading,
  },
};
