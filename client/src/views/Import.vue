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

      <div v-if="rawColumns.length>0" class="mt-3">
        <v-select
          v-for="(col, index) in rawColumns" :key="index"
          v-model="selectedColumns[index]"
          :items="options"
          class="mb-3"
          item-text="text"
          item-value="value">
        </v-select>
      </div>
      <v-btn
        :disabled="!valid"
        class="mr-3"
        @click="load">
        Загрузить
      </v-btn>
      <ClearButton :callback="clear"/>
    </v-card>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import FieldSelector from '@/components/FieldSelector.vue';
import { getTableData, parseStringTable } from '@/util/table';
import tables from '@/util/databaseTables';
import ClearButton from '@/components/buttons/ClearButton.vue';
import { validateNotEmptyColumns, validateRequiredColumn } from '../util/validator';
import BatchService from '../services/batch.service';

export default {
  name: 'Import',
  title: 'Импорт данных',
  components: { ClearButton, FieldSelector },
  data() {
    return {
      loaded: true,
      content: '',
      body: [],
      rawColumns: [],
      selectedColumns: [],
      dataTypes: [
        { value: 'wells', text: 'Скважины' },
        { value: 'horizons', text: 'Пласты' },
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
        text: row.text,
        value: row.value,
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

    parse() {
      const { header, body } = parseStringTable(this.content);
      this.rawColumns = header;
      this.body = body;
      this.selectedColumns = new Array(header.length);
      this.matchColumns();
    },

    matchColumns() {
      this.selectedColumns = this.rawColumns.map((col) => {
        const matched = tables[this.selectedDataType].find((el) => el.regex.test(col));
        return matched ? matched.value : '';
      });
    },

    async load() {
      const data = getTableData(this.selectedColumns, this.body);
      const payload = {
        field_id: this.field.id,
        rows: data,
      };
      console.log(payload);
      BatchService.load(this.selectedDataType, payload)
        .then(() => {
          console.log(payload);
          this.fetchField(this.field.id);
          this.fetchWells(this.field.id);
          if (this.well) {
            this.fetchWell(this.well.id);
          }
          this.$router.push('/main/db/wells');
        })
        .catch((err) => {
          console.log(payload);
          console.log(err);
        });
    },

    clear() {
      this.content = '';
      this.rawColumns = [];
      this.selectedColumns = [];
    },
  },
};
</script>
