<template>
  <div>
    <div v-if="this.field" class="container">
      <h2 class="text-center my-3">Импорт данных</h2>
      <b-card v-if="loaded">

        <!--        Datatype selector     -->
        <b-form inline>
          <label class="mr-sm-2">Тип данных</label>
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
          placeholder="Вставьте данные"
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
                  @click="load">Загрузить
        </b-button>
        <b-button class="mt-3 mr-3" variant="danger" @click="clear">Очистить</b-button>
      </b-card>
    </div>
    <div v-else>
      <h3 class="text-center my-3">Месторождение не выбрано
        <b-button @click="selectField">Выбрать</b-button>
      </h3>
    </div>
    <FieldSelector/>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import FieldSelector from '@/component/FieldSelector.vue';
import { getTableData, parseStringTable } from '@/util/table';
import tables from '@/util/databaseTables';
import { validateNotEmptyColumns, validateRequiredColumn } from '../util/validator';
import BatchService from '../service/BatchService';

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
        { value: 'coordinates', text: 'Координаты месторождения' },
      ],
      selectedDataType: 'wells',
    };
  },
  mounted() {
    if (!this.field) {
      if (localStorage.getItem('lastFieldId')) {
        this.fetchField(localStorage.getItem('lastFieldId'));
      } else {
        this.setSelectionVisible(true);
      }
    }
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
    load() {
      const data = getTableData(this.selectedColumns, this.body);
      const payload = {
        field_id: this.field.id,
        rows: data,
      };
      BatchService.load(this.selectedDataType, payload)
        .then((res) => {
          this.$toasted.show(res.data.message);
          this.fetchField(this.field.id);
          this.fetchWells(this.field.id);
          if (this.well) {
            this.fetchWell(this.well.id);
          }
        })
        .catch((err) => {
          this.$toasted.show('Ошибка загрузки данных');
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

<style scoped>

</style>
