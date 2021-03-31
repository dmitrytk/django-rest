<template>
  <v-container fluid>
    <FieldSelector/>

    <v-card class="ma-3 pa-3">
      <v-card-title v-if="field" primary-title>
        <div class="headline primary--text">{{ field.name }} месторождение
          <v-btn class="mr-3" color="primary" small @click="changeField">
            <v-icon>mdi-folder-open</v-icon>
          </v-btn>
        </div>
      </v-card-title>
      <v-card-text>
        <v-btn-toggle
          v-model="link"
          color="primary accent-3"
          group
          tile>
          <v-btn to="/main/db" value="wells">
            Скважины
          </v-btn>
          <v-btn to="/main/db/field" value="field">
            Данные месторождения
          </v-btn>

        </v-btn-toggle>
      </v-card-text>
    </v-card>

    <Wells/>

  </v-container>
</template>

<script>

import FieldSelector from '@/components/FieldSelector.vue';
import { mapActions, mapGetters } from 'vuex';
import Wells from './db/Wells.vue';

export default {
  name: 'Database',
  components: {
    Wells, FieldSelector,
  },
  data() {
    return {
      link: 'wells',
    };
  },
  mounted() {
    this.checkCurrentField();
  },
  computed: {
    ...mapGetters('fields', [
      'field',
      'fields',
      'selectionVisible',
    ]),
    ...mapGetters('wells', [
      'wells',
      'well',
    ]),
  },
  methods: {
    ...mapActions('fields', [
      'checkCurrentField',
      'setSelectionVisible',

    ]),
    changeField() {
      this.setSelectionVisible(true);
    },
  },
};
</script>

<style scoped>

</style>
