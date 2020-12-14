<template>
  <b-card-text v-if="currentWell">
    <!--String-->
    <b-form-group label="Номер" label-cols="4" label-cols-lg="2" label-for="input-default">
      <b-form-input v-model="currentWell.name"></b-form-input>
    </b-form-group>
    <b-form-group label="Куст" label-cols="4" label-cols-lg="2" label-for="input-default">
      <b-form-input v-model="currentWell.pad"></b-form-input>
    </b-form-group>
    <b-form-group label="Тип" label-cols="4" label-cols-lg="2" label-for="input-default">
      <b-form-input v-model="currentWell.type">
      </b-form-input>
    </b-form-group>
    <b-form-group label="Состояние" label-cols="4" label-cols-lg="2" label-for="input-default">
      <b-form-input v-model="currentWell.status">
      </b-form-input>
    </b-form-group>
    <!--Numeric-->
    <b-form-group label="Широта" label-cols="4" label-cols-lg="2" label-for="input-default">
      <b-form-input v-model="currentWell.lat" type="number">
      </b-form-input>
    </b-form-group>
    <b-form-group label="Долгота" label-cols="4" label-cols-lg="2" label-for="input-default">
      <b-form-input v-model="currentWell.lng" type="number">
      </b-form-input>
    </b-form-group>
    <b-form-group label="X" label-cols="4" label-cols-lg="2" label-for="input-default">
      <b-form-input v-model="currentWell.x" type="number">
      </b-form-input>
    </b-form-group>
    <b-form-group label="Y" label-cols="4" label-cols-lg="2" label-for="input-default">
      <b-form-input v-model="currentWell.y" type="number">
      </b-form-input>
    </b-form-group>
    <b-form-group label="Альтитуда" label-cols="4" label-cols-lg="2" label-for="input-default">
      <b-form-input v-model="currentWell.alt" type="number">
      </b-form-input>
    </b-form-group>
    <b-form-group label="Забой" label-cols="4" label-cols-lg="2" label-for="input-default">
      <b-form-input v-model="currentWell.bottom" type="number">
      </b-form-input>
    </b-form-group>
    <b-button variant="primary" @click="saveWell">Сохранить</b-button>
  </b-card-text>
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
        this.updateWell(this.currentWell);
      } else {
        console.log('save new well');
      }
    },
  },
};
</script>

<style scoped>

</style>
