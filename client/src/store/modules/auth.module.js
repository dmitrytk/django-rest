import { destroyToken, getToken, saveToken } from '@/commons/jwt';
import AuthService from '@/services/auth.service';
import router from '@/router';

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
    setLoggedIn(state, payload) {
      state.isLoggedIn = payload;
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
          saveToken(token);
          context.commit('setToken', token);
          context.commit('setLoggedIn', true);
          context.commit('setLogInError', false);
          await context.dispatch('getUserProfile');
          await context.dispatch('routeLoggedIn');
        }
      } catch (err) {
        context.commit('setLogInError', true);
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
    async logout(context) {
      await context.dispatch('removeLogIn');
      await context.dispatch('routeLogOut');
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
            await context.dispatch('removeLogIn');
          }
        } else {
          await context.dispatch('removeLogIn');
        }
      }
    },
    async removeLogIn({ commit }) {
      destroyToken();
      commit('setToken', '');
      commit('setLoggedIn', false);
    },
    // eslint-disable-next-line no-unused-vars
    routeLoggedIn(context) {
      router.push('/main');
    },
    // eslint-disable-next-line no-unused-vars
    routeLogOut(context) {
      if (router.currentRoute.path !== '/login') {
        router.push('/login');
      }
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
