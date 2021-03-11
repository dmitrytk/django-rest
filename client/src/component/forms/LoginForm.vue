<template>
  <b-card-text>
    <!--    EMAIL    -->
    <b-form-group label="Почта"
                  label-cols="4"
                  label-cols-lg="2"
                  label-for="input-default">
      <b-form-input v-model="email" required type="email">
      </b-form-input>
    </b-form-group>

    <!--    PASSWORD    -->
    <b-form-group label="Пароль"
                  label-cols="4"
                  label-cols-lg="2"
                  label-for="input-default">
      <b-form-input v-model="password" required type="password">
      </b-form-input>
    </b-form-group>
    <b-button variant="primary" @click="authenticate">Войти</b-button>
  </b-card-text>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'LoginForm',
  data() {
    return {
      email: null,
      password: null,
    };
  },
  methods: {
    ...mapActions('auth', ['login']),
    authenticate() {
      if (this.email && this.password) {
        const credentials = {
          user: {
            email: this.email,
            password: this.password,
          },
        };
        this.login(credentials);
      } else {
        this.$toasted.show('Некорректные данные');
      }
    },
  },
};
</script>

<style scoped>

</style>
