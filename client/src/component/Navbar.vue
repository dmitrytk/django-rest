<template>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand to="/">Horizon</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/db/wells">БД</b-nav-item>
        <b-nav-item to="/import">Импорт</b-nav-item>
        <b-nav-item to="/sandbox">Sandbox</b-nav-item>

        <b-nav-item-dropdown>
          <template v-slot:button-content>
            Инструменты
          </template>
          <b-dropdown-item to="/decline">Расчет понижений</b-dropdown-item>
          <b-dropdown-item to="/calculator">Водный калькулятор</b-dropdown-item>
          <b-dropdown-item to="/converter">Конвертер координат</b-dropdown-item>
          <b-dropdown-item to="/sql">SQL генератор</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input class="mr-sm-2" placeholder=" " size="sm"></b-form-input>
          <b-button class="my-2 my-sm-0" size="sm" type="submit">Искать</b-button>
        </b-nav-form>
        <b-nav-item v-if="this.field" class="font-italic" to="/db/wells">
          <ins>{{ this.field.name }}</ins>
        </b-nav-item>
        <b-nav-item v-if="this.field" class="font-italic">
          <b-icon class="clickable" icon="arrow-repeat" @click="changeDB()"></b-icon>
        </b-nav-item>
        <b-nav-item-dropdown v-if="user" right>
          <template v-slot:button-content>
            <em>{{ user }}</em>
          </template>
          <!--          <b-dropdown-item href="#">Профиль</b-dropdown-item>-->
          <b-dropdown-item href="#" @click="logout">Выйти</b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-item v-else to="/login">
          <ins>Войти</ins>
        </b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'Navbar',
  computed: {
    ...mapGetters('fields', [
      'field',
      'fields',
    ]),
    ...mapGetters('auth', [
      'user',
    ]),
  },
  methods: {
    ...mapActions('fields', [
      'setSelectionVisible',
    ]),
    ...mapActions('auth', [
      'logout',
    ]),
    changeDB() {
      this.setSelectionVisible(true);
    },

  },
};

</script>
