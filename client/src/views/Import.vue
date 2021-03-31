<template>
  <v-container fluid>
    <FieldSelector/>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Импорт данных</div>
      </v-card-title>

      <v-select
        v-model="selectedDataType"
        :items="dataTypes"
        item-text="text"
        item-value="value">

      </v-select>
      <v-textarea
        v-model="content"
        placeholder="Вставьте данные"
        @keyup="parse">
      </v-textarea>
    </v-card>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import FieldSelector from '@/components/FieldSelector.vue';
import { getTableData, parseStringTable } from '@/util/table';
import tables from '@/util/databaseTables';
import BatchService from '@/services/batch.service';
import { validateNotEmptyColumns, validateRequiredColumn } from '../util/validator';

export default {
  name: 'Import',
  title: 'Импорт данных',
  components: { FieldSelector },
  data() {
    return {
      loaded: true,
      content: '',
      body: [],
      rawColumns: [],
      selectedColumns: [],
      dataTypes: [
        { value: 'wells', text: 'Скважины' },
        { value: 'zones', text: 'Пласты' },
        { value: 'inclinometry', text: 'Инклинометрия' },
        { value: 'rates', text: 'Режимы' },
        { value: 'mer', text: 'МЭР' },
        { value: 'cases', text: 'Обсадные колонны' },
        { value: 'perforations', text: 'Интервалы перфорации' },
        { value: 'pumps', text: 'Насосы' },
        { value: 'coordinates', text: 'Координаты месторождения' },
      ],
      selectedDataType: 'wells',
    };
  },
  mounted() {
    this.checkCurrentField();
  },
  computed: {
    ...mapGetters('fields', [
      'field',
    ]),
    ...mapGetters('wells', [
      'well',
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
      'checkCurrentField',
      'fetchField',
      'setSelectionVisible',
    ]),
    ...mapActions('wells', [
      'fetchWells',
      'fetchWell',
    ]),
    selectField() {
      this.setSelectionVisible(true);
    },
    matchColumns() {
      this.selectedColumns = this.rawColumns.map((col) => {
        const matched = tables[this.selectedDataType].find((el) => el.regex.test(col));
        return matched ? matched.key : '';
      });
    },
    async load() {
      const data = getTableData(this.selectedColumns, this.body);
      const payload = {
        field_id: this.field.id,
        rows: data,
      };
      BatchService.load(this.selectedDataType, payload)
        .then((res) => {
          console.log(res.data.message);
          this.fetchField(this.field.id);
          this.fetchWells(this.field.id);
          if (this.well) {
            this.fetchWell(this.well.id);
          }
          this.$router.push('/main/db');
        })
        .catch((err) => {
          console.log(err);
        });
    },
    parse() {
      const { header, body } = parseStringTable(this.content);
      this.rawColumns = header;
      this.body = body;
      this.selectedColumns = new Array(header.length);
      this.matchColumns();
    },
    clear() {
      this.content = '';
      this.rawColumns = [];
      this.selectedColumns = [];
    },
  },
};
</script>
