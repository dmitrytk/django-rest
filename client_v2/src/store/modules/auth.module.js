import { destroyToken, getToken, saveToken } from '@/common/jwt';
import AuthService from '../../service/auth.service';
import router from '../../router';

export default {
  namespaced: true,
  state: () => (
    {
      token: null,
      isLoggedIn: null,
      logInError: null,
      userProfile: null,
    }
  ),
  mutations: {
    setToken(state, token) {
      state.token = token;
    },
    setLoggedIn(state) {
      state.isLoggedIn = true;
    },
    setLogInError(state, payload) {
      state.logInError = payload;
    },
    setUserProfile(state, payload) {
      state.userProfile = payload;
    },

  },
  actions: {
    async login(context, credentials) {
      try {
        const response = await AuthService.login(credentials);
        const token = response.data.access;
        if (token) {
          console.log('login success');
          saveToken(token);
          context.commit('setToken', token);
          context.commit('setLoggedIn', true);
          context.commit('setLogInError', false);
          await context.dispatch('getUserProfile');
          await context.dispatch('routeLoggedIn');
        }
      } catch (err) {
        await context.dispatch('checkApiError', err);
      }
    },
    async getUserProfile({ commit }) {
      try {
        const response = await AuthService.getUserProfile();
        if (response.data) {
          commit('setUserProfile', response.data);
        }
      } catch (err) {
        console.log(err);
      }
    },
    async logout({ commit }) {
      console.log('logout');
      destroyToken();
      commit('setToken', null);
      commit('setLoggedIn', false);
      router.push('/');
    },
    async checkLoggedIn(context) {
      if (!context.state.isLoggedIn) {
        let { token } = context.state;
        if (!token) {
          const localToken = getToken();
          if (localToken) {
            context.commit('setToken', localToken);
            token = localToken;
          }
        }
        if (token) {
          try {
            const response = await AuthService.getUserProfile();
            context.commit('setLoggedIn', true);
            context.commit('setUserProfile', response.data);
          } catch (error) {
            await context.dispatch('logout');
          }
        } else {
          await context.dispatch('logout');
        }
      }
    },
    // eslint-disable-next-line no-unused-vars
    routeLoggedIn(context) {
      router.push('/db');
    },
    async checkApiError(context, payload) {
      if (payload.response.status === 401) {
        await context.dispatch('logout');
      }
    },
  },
  getters: {
    userProfile: (state) => state.userProfile,
    isLoggedIn: (state) => state.isLoggedIn,
    logInError: (state) => state.logInError,
    token: (state) => state.token,
  },
};
