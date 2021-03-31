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
      zones: null,
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
    setZones(state, payload) {
      state.zones = payload;
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
    async fetchFields({ commit }) {
      const fields = await FieldService.findAll();
      commit('setFields', fields.data);
    },
    async fetchField(context, id) {
      const field = await FieldService.findOne(id);
      localStorage.setItem('lastFieldId', field.data.id);
      context.commit('setField', field.data);
      context.commit('setSelectionVisible', false);
      context.dispatch('fetchFieldData', id);
    },
    async fetchFieldData(context, id) {
      context.dispatch('fetchInclinometry', id);
      context.dispatch('fetchMer', id);
      context.dispatch('fetchRates', id);
      context.dispatch('fetchZones', id);
      context.dispatch('fetchCoordinates', id);
    },
    async updateField(context, data) {
      const field = await FieldService.update(data.id, data);
      context.commit('setField', field.data);
      await context.dispatch('fetchFields');
    },
    async fetchInclinometry({ commit }, id) {
      const res = await FieldService.getInclinometry(id);
      commit('setInclinometry', res.data);
    },
    async fetchMer({ commit }, id) {
      const res = await FieldService.getMer(id);
      commit('setMer', res.data);
    },
    async fetchRates({ commit }, id) {
      const res = await FieldService.getRates(id);
      commit('setRates', res.data);
    },
    async fetchZones({ commit }, id) {
      const res = await FieldService.getZones(id);
      commit('setZones', res.data);
    },
    async fetchCoordinates({ commit }, id) {
      const res = await FieldService.getCoordinates(id);
      commit('setCoordinates', res.data);
    },

    // DELETE CHILD OBJECTS
    async deleteInclinometry(context, id) {
      await FieldService.deleteInclinometry(id);
    },
    async deleteMer(context, id) {
      await FieldService.deleteMer(id);
    },
    async deleteRates(context, id) {
      await FieldService.deleteRates(id);
    },
    async deleteZones(context, id) {
      await FieldService.deleteZones(id);
    },
    async deleteCoordinates(context, id) {
      await FieldService.deleteCoordinates(id);
    },

    setSelectionVisible({ commit }, payload) {
      commit('setSelectionVisible', payload);
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
    zones: (state) => state.zones,
    coordinates: (state) => state.coordinates,
  },
};
