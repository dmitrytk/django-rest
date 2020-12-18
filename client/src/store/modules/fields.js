import FieldService from '@/service/FieldService';

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
    setCoordinates(state, payload) {
      state.coordinates = payload;
    },
  },
  actions: {
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
    async fetchCoordinates({ commit }, id) {
      const res = await FieldService.getCoordinates(id);
      commit('setCoordinates', res.data);
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
    coordinates: (state) => state.coordinates,
  },
};
