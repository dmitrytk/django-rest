<template>
  <div>
    <div v-if="this.field" class="container">
      <h2 class="text-center my-3">Import data to {{ this.field.name }} field</h2>
      <b-card v-if="loaded">
        <b-form inline>
          <label class="mr-sm-2">Data type</label>
          <b-form-select
            v-model="selectedDataType"
            :options="dataTypes"
            class="mb-2 mr-sm-2 mb-sm-0"
          ></b-form-select>
        </b-form>
        <b-form-textarea
          v-model="content"
          class="mt-3"
          max-rows="10"
          placeholder="Insert data here"
          rows="10"
          @keyup="parse"
        ></b-form-textarea>
        <b-button class="mt-3 mr-3" variant="primary" @click="load">Load</b-button>
        <b-button class="mt-3 mr-3" variant="danger" @click="clear">Clear</b-button>
      </b-card>
    </div>
    <div v-else>
      <h3 class="text-center my-3">No field Selected
        <b-button @click="selectField">Select field</b-button>
      </h3>

    </div>
    <FieldSelector/>
  </div>

</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import FieldSelector from '@/component/FieldSelector.vue';

export default {
  name: 'Import',
  components: { FieldSelector },
  data() {
    return {
      loaded: true,
      content: '',
      dataTypes: [
        { value: 'wells', text: 'Wells' },
        { value: 'zones', text: 'Zones' },
        { value: 'inclinometry', text: 'Inclinometry' },
        { value: 'rates', text: 'Rates' },
        { value: 'mer', text: 'MER' },
        { value: 'coordinates', text: ' Field Coordinates' },
      ],
      selectedDataType: 'wells',
    };
  },
  mounted() {
    if (!this.field) {
      this.setSelectionVisible(true);
    }
  },
  computed: {
    ...mapGetters('fields', [
      'field',
    ]),
  },
  methods: {
    ...mapActions('fields', [
      'setSelectionVisible',
    ]),
    selectField() {
      this.setSelectionVisible(true);
    },
    parse() {
      console.log('parse');
    },
    load() {
      console.log('load');
    },
    clear() {
      this.content = '';
    },
  },
};
</script>

<style scoped>

</style>
