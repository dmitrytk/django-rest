<template>
  <b-card-text v-if="currentField">
    <!--String-->
    <b-form-group label="Name" label-cols="4" label-cols-lg="2" label-for="input-default">
      <b-form-input v-model="currentField.name"></b-form-input>
    </b-form-group>
    <b-form-group label="Type" label-cols="4" label-cols-lg="2" label-for="input-default">
      <b-form-input v-model="currentField.type"></b-form-input>
    </b-form-group>
    <b-form-group label="Location" label-cols="4" label-cols-lg="2" label-for="input-default">
      <b-form-input v-model="currentField.location">
      </b-form-input>
    </b-form-group>
    <b-button variant="primary" @click="saveField">Сохранить</b-button>
  </b-card-text>
</template>

<script>

import { mapActions, mapGetters } from 'vuex';
import _ from 'lodash';

export default {
  name: 'FieldForm',
  data() {
    return {
      currentField: {},
    };
  },
  computed: {
    ...mapGetters('fields', [
      'field',
    ]),
  },
  watch: {
    field: {
      handler() {
        this.currentField = _.cloneDeep(this.field);
      },
      immediate: true,
    },
  },
  methods: {
    ...mapActions('fields', [
      'updateField',
    ]),
    saveField() {
      if (this.currentField.id) {
        const result = _.mapValues(this.currentField, (v) => (v === '' ? null : v));
        this.updateField(result);
      } else {
        console.log('save new well');
      }
    },
  },
};
</script>

<style scoped>

</style>
