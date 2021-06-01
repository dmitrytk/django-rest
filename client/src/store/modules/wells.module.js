import WellService from '@/services/well.service';
import FieldService from '@/services/field.service';

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
      horizons: null,
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
    setHorizons(state, payload) {
      state.horizons = payload;
    },
  },
  actions: {
    async checkCurrentWells(context) {
      if (!context.state.wells) {
        const lastFieldId = localStorage.getItem('lastFieldId');
        if (lastFieldId) await context.dispatch('fetchWells', lastFieldId);
      }
    },
    async fetchWell(context, id) {
      try {
        context.commit('setWellLoading', true);
        const well = await WellService.findOne(id);
        context.dispatch('fetchWellData', id);
        context.commit('setWell', well.data);
        context.commit('setWellLoading', false);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async deleteWell({ dispatch }, id) {
      try {
        WellService.delete(id);
      } catch (err) {
        dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchWells(context, fieldId) {
      try {
        context.commit('setWellsLoading', true);
        const wells = await FieldService.getWells(fieldId);
        context.commit('setWells', wells.data);
        context.commit('setWellsLoading', false);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchWellData({ dispatch }, id) {
      dispatch('fetchInclinometry', id);
      dispatch('fetchMer', id);
      dispatch('fetchRates', id);
      dispatch('fetchHorizons', id);
      dispatch('fetchCases', id);
      dispatch('fetchPerforations', id);
      dispatch('fetchPumps', id);
    },

    // GET CHILD OBJECTS
    async fetchInclinometry(context, id) {
      try {
        const res = await WellService.getInclinometry(id);
        context.commit('setInclinometry', res.data);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchMer(context, id) {
      try {
        const res = await WellService.getMer(id);
        context.commit('setMer', res.data);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchRates(context, id) {
      try {
        const res = await WellService.getRates(id);
        context.commit('setRates', res.data);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchHorizons(context, id) {
      try {
        const res = await WellService.getHorizons(id);
        context.commit('setHorizons', res.data);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchCases(context, id) {
      try {
        const res = await WellService.getCases(id);
        context.commit('setCases', res.data);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchPerforations(context, id) {
      try {
        const res = await WellService.getPerforations(id);
        context.commit('setPerforations', res.data);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchPumps(context, id) {
      try {
        const res = await WellService.getPumps(id);
        context.commit('setPumps', res.data);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },

    // DELETE CHILD OBJECTS
    async deleteInclinometry({ dispatch }, id) {
      try {
        await WellService.deleteInclinometry(id);
      } catch (err) {
        dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async deleteMer({ dispatch }, id) {
      try {
        await WellService.deleteMer(id);
      } catch (err) {
        dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async deleteRates({ dispatch }, id) {
      try {
        await WellService.deleteRates(id);
      } catch (err) {
        dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async deleteHorizons({ dispatch }, id) {
      try {
        await WellService.deleteHorizons(id);
      } catch (err) {
        dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async deleteCases({ dispatch }, id) {
      try {
        await WellService.deleteCases(id);
      } catch (err) {
        dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async deletePerforations({ dispatch }, id) {
      try {
        await WellService.deletePerforations(id);
      } catch (err) {
        dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async deletePumps({ dispatch }, id) {
      try {
        await WellService.deletePumps(id);
      } catch (err) {
        dispatch('auth/checkApiError', err, { root: true });
      }
    },

    async updateWell(context, data) {
      try {
        const well = await WellService.update(data.id, data);
        await context.dispatch('fetchWell', well.data.id);
        await context.dispatch('fetchWells', well.data.field);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
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
    horizons: (state) => state.horizons,
    cases: (state) => state.cases,
    perforations: (state) => state.perforations,
    pumps: (state) => state.pumps,

  },
};
