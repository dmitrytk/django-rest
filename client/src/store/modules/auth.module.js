import Vue from 'vue';
import { getToken } from '../../common/jwt';
import AuthService from '../../service/auth.service';
import Router from '../../router';

export default {
  namespaced: true,
  state: () => (
    {
      user: null,
      isAuthenticated: getToken(),
    }
  ),
  mutations: {
    loginSuccess(state, user) {
      state.isAuthenticated = true;
      state.user = user.user.username;
      console.log(state.user);
      Router.push('/db');
    },
    loginFailure(state) {
      state.isAuthenticated = false;
      state.user = null;
      Vue.toasted.show('Пользователь с такими почтой и паролем не найден');
    },
    logout(state) {
      state.isAuthenticated = false;
      state.user = null;
      Router.push('/');
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
    isAuthenticated: (state) => state.isAuthenticated,
  },
};
