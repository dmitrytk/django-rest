<template>
  <div>
    <b-modal
      v-model="visible"
      no-fade
      title="Database"
      @ok="loadField"
    >
      <b-form-select
        v-if="this.fields"
        v-model="selectedFieldId"
        :options="fieldList">
        <template #first>
          <b-form-select-option :value="null" disabled>
            -- Выберите месторождение --
          </b-form-select-option>
        </template>
      </b-form-select>
    </b-modal>
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
    },
  },
};
</script>

<style scoped>

</style>
