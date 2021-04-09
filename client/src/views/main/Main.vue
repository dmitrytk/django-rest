<template>
  <v-app>
    <!--    Side Nav    -->
    <v-navigation-drawer v-model="drawer" app>
      <v-subheader>Меню</v-subheader>
      <v-list flat nav>
        <v-list-item-group color="primary">
          <v-list-item
            v-for="item in items"
            :key="item.title"
            :to="item.to"
            link>
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
        <v-list-group no-action prepend-icon="mdi-tools">
          <template v-slot:activator>
            <v-list-item-title>Инструменты</v-list-item-title>
          </template>
          <v-list-item
            v-for="([title, to], i) in tools"
            :key="i"
            :to="to" link>
            <v-list-item-title v-text="title"></v-list-item-title>
          </v-list-item>

        </v-list-group>
      </v-list>

      <!--      Bottom nav      -->
      <template v-slot:append>
        <v-list-item link @click="logout">
          <v-list-item-icon>
            <v-icon>mdi-close</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-navigation-drawer>

    <!--    App Bar    -->
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>{{ appName }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-menu bottom left>
        <template v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" icon>
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="n in 2"
            :key="n"
            @click="() => {}">
            <v-list-item-title>Option {{ n }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <!--    Main content    -->
    <v-main>
      <router-view></router-view>
    </v-main>

    <!--    Footer    -->
    <v-footer app class="pa-3" fixed>
      <v-spacer></v-spacer>
      <span>&copy; {{ appName }}</span>
    </v-footer>
  </v-app>
</template>

<script>

import { appName } from '@/commons/config';
import { mapActions } from 'vuex';

const routeGuardMain = async (to, from, next) => {
  if (to.path === '/main') {
    next('/main/dashboard');
  } else {
    next();
  }
};

export default {
  name: 'Main',
  data() {
    return {
      appName,
      drawer: null,
      items: [
        { title: 'Главная', icon: 'mdi-home', to: '/main/dashboard' },
        { title: 'База данных', icon: 'mdi-database', to: '/main/db/wells' },
        { title: 'Импорт', icon: 'mdi-application-import', to: '/main/import' },
      ],
      tools: [
        ['Конвертер координат', '/main/tools/converter'],
        ['Расчет понижений', '/main/tools/decline'],
        ['SQL Генератор', '/main/tools/sql'],
        ['Калькулятор', '/main/tools/calculator'],
      ],
    };
  },
  beforeRouteEnter(to, from, next) {
    routeGuardMain(to, from, next);
  },

  beforeRouteUpdate(to, from, next) {
    routeGuardMain(to, from, next);
  },

  methods: {
    ...mapActions('auth', [
      'logout',
    ]),
  },

};
</script>
