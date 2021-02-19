import { getToken } from '../../common/jwt';
import AuthService from '../../service/auth.service';

export default {
  namespaced: true,
  state: () => (
    {
      user: {},
      isAuthenticated: getToken(),
    }
  ),
  mutations: {
    loginSuccess(state, user) {
      state.isAuthenticated = true;
      state.user = user;
    },
    loginFailure(state) {
      state.isAuthenticated = false;
      state.user = null;
    },
    logout(state) {
      state.isAuthenticated = false;
      state.user = null;
    },
  },
  actions: {
    login({ commit }, credentials) {
      return AuthService.login(credentials).then((user) => {
        commit('loginSuccess', user);
        return Promise.resolve(user);
      },
      (error) => {
        commit('loginFailure');
        return Promise.reject(error);
      });
    },
    logout({ commit }) {
      AuthService.logout();
      commit('logout');
    },
  },
  getters: {
    user: (state) => state.user,
  },
};
