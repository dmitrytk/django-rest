<template>
  <div v-if="currentWell">
    <!--String-->
    <v-text-field v-model="currentWell.name" label="Номер" type="text"></v-text-field>
    <v-text-field v-model="currentWell.pad" label="Куст" type="text"></v-text-field>
    <v-text-field v-model="currentWell.type" label="Тип" type="text"></v-text-field>
    <v-text-field v-model="currentWell.status" label="Состояние" type="text"></v-text-field>
    <!--Numeric-->
    <v-text-field v-model="currentWell.lat" label="Широта" type="number"></v-text-field>
    <v-text-field v-model="currentWell.lng" label="Долгота" type="number"></v-text-field>
    <v-text-field v-model="currentWell.x" label="X" type="number"></v-text-field>
    <v-text-field v-model="currentWell.y" label="Y" type="number"></v-text-field>
    <v-text-field v-model="currentWell.alt" label="Альтитуда" type="number"></v-text-field>
    <v-text-field v-model="currentWell.bottom" label="Забой" type="number"></v-text-field>
    <v-btn color="primary" @click="saveWell">Сохранить</v-btn>
  </div>

</template>

<script>

import { mapActions, mapGetters } from 'vuex';
import _ from 'lodash';

export default {
  name: 'WellForm',
  data() {
    return {
      currentWell: {},
    };
  },
  computed: {
    ...mapGetters('wells', [
      'well',
    ]),
  },
  watch: {
    well: {
      handler() {
        this.currentWell = _.cloneDeep(this.well);
      },
      immediate: true,
    },
  },
  methods: {
    ...mapActions('wells', [
      'updateWell',
    ]),
    saveWell() {
      if (this.currentWell.id) {
        const result = _.mapValues(this.currentWell, (v) => (v === '' ? null : v));
        this.updateWell(result);
      } else {
        console.log('save new well');
      }
    },
  },
};
</script>

<style scoped>

</style>
