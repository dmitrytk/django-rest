<template>
  <v-main>
    <v-container fill-height fluid>
      <v-layout align-center justify-center>
        <v-flex md4 sm8 xs12>
          <v-card class="elevation-12">
            <v-toolbar color="primary" dark>
              <v-toolbar-title>{{ appName }}</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
            <v-card-text>
              <v-form @keyup.enter="submit">
                <v-text-field v-model="username"
                              label="Имя пользователя"
                              name="login"
                              prepend-inner-icon="mdi-account"
                              @keyup.enter="submit"></v-text-field>
                <v-text-field id="password"
                              v-model="password"
                              label="Пароль"
                              name="password"
                              prepend-inner-icon="mdi-lock"
                              type="password"
                              @keyup.enter="submit"></v-text-field>
              </v-form>
              <div v-if="logInError">
                <v-alert :value="logInError" transition="fade-transition" type="error">
                  Неверное имя пользоваетля или пароль.
                </v-alert>
              </div>
              <!--              <v-flex class="caption text-xs-right">-->
              <!--                <router-link to="/recover-password">-->
              <!--                  Forgot your password?-->
              <!--                </router-link>-->
              <!--              </v-flex>-->
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click.prevent="submit">Login</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import { appName } from '../commons/config';

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      appName,
    };
  },
  computed: {
    ...mapGetters('auth', [
      'logInError',
    ]),
  },

  methods: {
    ...mapActions('auth', [
      'login',
    ]),

    submit() {
      this.login({ username: this.username, password: this.password });
    },
  },
};
</script>

<style scoped>

</style>
