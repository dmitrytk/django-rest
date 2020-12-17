<template>
  <div>
    <div v-if="this.field" class="container">
      <h2 class="text-center my-3">Import data to {{ this.field.name }} field</h2>
      <b-card v-if="loaded">

        <!--        Datatype selector     -->
        <b-form inline>
          <label class="mr-sm-2">Data type</label>
          <b-form-select
            v-model="selectedDataType"
            :options="dataTypes"
            class="mb-2 mr-sm-2 mb-sm-0"
          ></b-form-select>
        </b-form>

        <!--        Textarea      -->
        <b-form-textarea
          v-model="content"
          class="mt-3"
          max-rows="10"
          placeholder="Insert data here"
          rows="10"
          @keyup="parse"
        ></b-form-textarea>

        <!--   Column selector     -->
        <div v-if="rawColumns.length>0" class="mt-3">
          <b-form-group v-for="(col, index) in rawColumns" :key="index"
                        :label="col"
                        label-cols="4"
                        label-cols-lg="2" label-for="input-sm"
                        label-size="sm">
            <b-form-select
              v-model="selectedColumns[index]"
              :options="options"
              class="mb-3">
            </b-form-select>
          </b-form-group>
        </div>
        <b-button :disabled="!valid"
                  class="mt-3 mr-3"
                  variant="primary"
                  @click="load">Load
        </b-button>
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
import getTableData from '@/util/table';
import tables from '@/util/databaseTables';
import { validateNotEmptyColumns, validateRequiredColumn } from '../util/validator';

const mockData = `well\tx\ty
331R\t13566588.5\t6739251.165
335R\t13561534.8\t6734774.297
337R\t13566221.62\t6744041.206
340R\t13562965.11\t6743459.514
341R\t13564186.93\t6748381.851
342R\t13555210.76\t6741187.011
`;

export default {
  name: 'Import',
  components: { FieldSelector },
  data() {
    return {
      loaded: true,
      content: '',
      rawColumns: [],
      selectedColumns: [],
      dataTypes: [
        { value: 'wells', text: 'Wells' },
        { value: 'zones', text: 'Zones' },
        { value: 'inclinometry', text: 'Inclinometry' },
        { value: 'rates', text: 'Rates' },
        { value: 'mer', text: 'MER' },
        { value: 'coordinates', text: 'Field Coordinates' },
      ],
      selectedDataType: 'wells',
    };
  },
  mounted() {
    if (!this.field) {
      this.setSelectionVisible(true);
    }
    this.parse();
    this.matchColumns();
  },
  computed: {
    ...mapGetters('fields', [
      'field',
    ]),
    options() {
      return tables[this.selectedDataType].map((row) => ({
        text: row.label,
        value: row.key,
      }));
    },
    valid() {
      return this.selectedColumns.length > 0
        && validateNotEmptyColumns(this.selectedColumns)
        && validateRequiredColumn(this.selectedColumns, tables[this.selectedDataType]);
    },
  },
  methods: {
    ...mapActions('fields', [
      'setSelectionVisible',
    ]),
    selectField() {
      this.setSelectionVisible(true);
    },
    matchColumns() {
      this.selectedColumns = this.rawColumns.map((col) => {
        const matched = tables[this.selectedDataType].find((el) => el.regex.test(col));
        return matched ? matched.key : '';
      });
      console.log(this.selectedColumns);
    },
    load() {
      console.log(this.selectedColumns);
    },
    parse() {
      const { header } = getTableData(mockData);
      this.rawColumns = header;
      this.selectedColumns = new Array(header.length);
    },
    clear() {
      this.content = '';
      this.rawColumns = [];
      this.selectedColumns = [];
    },
  },
};
</script>

<style scoped>

</style>
