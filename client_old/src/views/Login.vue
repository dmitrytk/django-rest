<template>
  <b-container>
    <h2 class="text-center my-3">Войти</h2>
    <b-card>
      <LoginForm/>
    </b-card>
  </b-container>
</template>
<script>

import LoginForm from '@/component/forms/LoginForm.vue';

export default {
  name: 'Login',
  title: 'Login',
  components: { LoginForm },
  data() {
    return {};
  },
  methods: {},
};
</script>
