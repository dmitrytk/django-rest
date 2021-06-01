import FieldService from '@/services/field.service';

export default {
  namespaced: true,
  state: () => (
    {
      field: null,
      fields: null,
      fieldLoading: false,
      fieldsLoading: false,
      selectionVisible: false,
      inclinometry: null,
      mer: null,
      rates: null,
      horizons: null,
      coordinates: null,
    }
  ),
  mutations: {
    setFieldsLoading(state, IsLoading) {
      state.fieldsLoading = IsLoading;
    },
    setFieldLoading(state, IsLoading) {
      state.fieldLoading = IsLoading;
    },
    setField(state, payload) {
      state.field = payload;
    },
    setFields(state, payload) {
      state.fields = payload;
    },
    setSelectionVisible(state, payload) {
      state.selectionVisible = payload;
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
    setHorizons(state, payload) {
      state.horizons = payload;
    },
    setCoordinates(state, payload) {
      state.coordinates = payload;
    },
  },
  actions: {
    async checkCurrentField(context) {
      if (!context.state.field) {
        const lastFieldId = localStorage.getItem('lastFieldId');
        if (lastFieldId) await context.dispatch('fetchField', lastFieldId);
        else {
          context.commit('setSelectionVisible', true);
        }
      }
    },
    async fetchFields(context) {
      try {
        const fields = await FieldService.findAll();
        context.commit('setFields', fields.data);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchField(context, id) {
      try {
        const field = await FieldService.findOne(id);
        localStorage.setItem('lastFieldId', field.data.id);
        context.commit('setField', field.data);
        context.commit('setSelectionVisible', false);
        context.dispatch('fetchFieldData', id);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchFieldData(context, id) {
      try {
        context.dispatch('fetchInclinometry', id);
        context.dispatch('fetchMer', id);
        context.dispatch('fetchRates', id);
        context.dispatch('fetchHorizons', id);
        context.dispatch('fetchCoordinates', id);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async updateField(context, data) {
      try {
        const field = await FieldService.update(data.id, data);
        context.commit('setField', field.data);
        await context.dispatch('fetchFields');
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchInclinometry(context, id) {
      try {
        const res = await FieldService.getInclinometry(id);
        context.commit('setInclinometry', res.data);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchMer(context, id) {
      try {
        const res = await FieldService.getMer(id);
        context.commit('setMer', res.data);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchRates(context, id) {
      try {
        const res = await FieldService.getRates(id);
        context.commit('setRates', res.data);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchHorizons(context, id) {
      try {
        const res = await FieldService.getHorizons(id);
        console.log('fetched horizons:');
        console.log(res.data);
        context.commit('setHorizons', res.data);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async fetchCoordinates(context, id) {
      try {
        const res = await FieldService.getCoordinates(id);
        context.commit('setCoordinates', res.data);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },

    // DELETE CHILD OBJECTS
    async deleteInclinometry(context, id) {
      try {
        await FieldService.deleteInclinometry(id);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async deleteMer(context, id) {
      try {
        await FieldService.deleteMer(id);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async deleteRates(context, id) {
      try {
        await FieldService.deleteRates(id);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async deleteHorizons(context, id) {
      try {
        await FieldService.deleteHorizons(id);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },
    async deleteCoordinates(context, id) {
      try {
        await FieldService.deleteCoordinates(id);
      } catch (err) {
        context.dispatch('auth/checkApiError', err, { root: true });
      }
    },

    setSelectionVisible(context, payload) {
      context.commit('setSelectionVisible', payload);
    },
  },
  getters: {
    field: (state) => state.field,
    fields: (state) => state.fields,
    fieldLoading: (state) => state.fieldLoading,
    fieldsLoading: (state) => state.fieldsLoading,
    selectionVisible: (state) => state.selectionVisible,
    inclinometry: (state) => state.inclinometry,
    mer: (state) => state.mer,
    rates: (state) => state.rates,
    fieldHorizons: (state) => state.horizons,
    coordinates: (state) => state.coordinates,
  },
};
