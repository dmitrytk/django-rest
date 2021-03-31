<template>
  <div v-if="currentField">
    <!--String-->
    <v-text-field v-model="currentField.name" label="Название"></v-text-field>
    <v-text-field v-model="currentField.type" label="Тип"></v-text-field>
    <v-text-field v-model="currentField.location" label="Местонахождение"></v-text-field>
    <v-btn color="primary" @click="saveField">Сохранить</v-btn>
  </div>
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
