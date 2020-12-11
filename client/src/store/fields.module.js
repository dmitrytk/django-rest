import FieldService from '@/service/FieldService';

export default {
  namespaced: true,
  state: () => (
    {
      field: null,
      fields: null,
      isLoading: false,
    }
  ),
  mutations: {
    setField(state, payload) {
      state.field = payload;
    },
    setFields(state, payload) {
      state.fields = payload;
    },
  },
  actions: {
    async fetchFields(context) {
      const fields = await FieldService.findAll();
      context.commit('setFields', fields.data);
    },
    async fetchField(context, id) {
      const field = await FieldService.findOne(id);
      context.commit('setField', field.data);
    },
  },
  getters: {
    fields: (state) => state.fields,
    field: (state) => state.field,
    isLoading: (state) => state.isLoading,
  },
};
