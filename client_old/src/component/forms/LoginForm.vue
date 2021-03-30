<template>
  <b-card-text>
    <!--    EMAIL    -->
    <b-form @submit="authenticate">
      <b-form-group label="Имя пользователя"
                    label-cols="4"
                    label-cols-lg="2"
                    label-for="input-default">
        <b-form-input v-model="username" required type="text">
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
      <b-button type="submit" variant="primary">Войти</b-button>
    </b-form>
  </b-card-text>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'LoginForm',
  data() {
    return {
      username: 'admin',
      password: null,
    };
  },
  methods: {
    ...mapActions('auth', ['login']),
    authenticate(event) {
      event.preventDefault();
      if (this.username && this.password) {
        const credentials = {
          username: this.username,
          password: this.password,
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
