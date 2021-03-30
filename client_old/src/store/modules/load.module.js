import tables from '@/util/databaseTables';

export default {
  namespaced: true,
  state: () => (
    {
      content: '',
      tableName: null,
      columns: [],
      tables,
    }
  ),
  mutations: {
    setContent(state, payload) {
      state.content = payload;
    },
  },
  actions: {},
  getters: {},
};
