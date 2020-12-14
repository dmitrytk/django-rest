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
            -- Select field --
          </b-form-select-option>
        </template>
      </b-form-select>
    </b-modal>
    <b-button class="mt-3" @click="changeDB">Change DB</b-button>

  </div>

</template>

<script>

import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'FieldSelector',
  data() {
    return {
      visible: false,
      selectedFieldId: null,
    };
  },
  mounted() {
    if (!this.fields) {
      this.fetchFields();
      this.visible = true;
    }
  },
  computed: {
    ...mapGetters('fields', [
      'field',
      'fields',
    ]),
    fieldList() {
      return this.fields.map((field) => ({ text: field.name, value: field.id }));
    },
  },
  methods: {
    ...mapActions('fields', [
      'fetchFields',
      'fetchField',
    ]),
    ...mapActions('wells', [
      'fetchWells',
    ]),
    loadField() {
      this.fetchField(this.selectedFieldId);
      this.fetchWells(this.selectedFieldId);
      this.visible = false;
    },
    changeDB() {
      this.visible = true;
    },
  },
};
</script>

<style scoped>

</style>
