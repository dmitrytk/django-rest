export default {
  namespaced: true,
  state: () => (
    {
      well: null,
      isLoading: false,
    }
  ),
  mutations: {
    setWell(state, payload) {
      state.well = payload;
    },
  },
  actions: {},
  getters: {},
};
