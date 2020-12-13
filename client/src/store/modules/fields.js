import FieldService from '@/service/FieldService';

export default {
  namespaced: true,
  state: () => (
    {
      field: null,
      fields: null,
      fieldLoading: false,
      fieldsLoading: false,
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
  },
  actions: {
    async fetchFields({ commit }) {
      commit('setFieldsLoading', true);
      const fields = await FieldService.findAll();
      commit('setFields', fields.data);
      commit('setFieldsLoading', false);
    },
    async fetchField({ commit }, id) {
      commit('setFieldLoading', true);
      const field = await FieldService.findOne(id);
      commit('setField', field.data);
      commit('setFieldLoading', false);
    },
  },
  getters: {
    field: (state) => state.field,
    fields: (state) => state.fields,
    fieldLoading: (state) => state.fieldLoading,
    fieldsLoading: (state) => state.fieldsLoading,
  },
};
