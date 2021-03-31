<template>
  <div>
    <v-dialog
      v-model="visible"
      width="500">
      <v-card>
        <v-card-title class="headline grey lighten-2">
          Выберите месторождение
        </v-card-title>

        <v-card-text class="pb-0 mt-3">
          <v-select
            v-if="fields"
            v-model="selectedFieldId"
            :items="fields"
            item-text="name"
            item-value="id"
            label="Месторождение">
          </v-select>
          <p v-else>Не удается загрузить месторождения</p>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="loadField">
            Выбрать
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>

import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'FieldSelector',
  data() {
    return {
      selectedFieldId: null,
    };
  },
  mounted() {
    if (!this.fields) {
      this.fetchFields();
    }
    if (this.field) {
      this.selectedFieldId = this.field.id;
    }
  },
  computed: {
    ...mapGetters('fields', [
      'field',
      'fields',
      'selectionVisible',
    ]),
    fieldList() {
      return this.fields.map((field) => ({ text: field.name, value: field.id }));
    },
    visible: {
      get() {
        return this.selectionVisible;
      },
      set(value) {
        this.setSelectionVisible(value);
      },
    },

  },
  methods: {
    ...mapActions('fields', [
      'fetchFields',
      'fetchField',
      'setSelectionVisible',
    ]),
    ...mapActions('wells', [
      'fetchWells',
    ]),
    loadField() {
      this.fetchField(this.selectedFieldId);
      this.fetchWells(this.selectedFieldId);
      this.$store.commit('wells/setWell', null);
      this.visible = false;
      // this.$store.commit('fields/setSelectionVisible', false);
    },
  },
};
</script>

<style scoped>

</style>
