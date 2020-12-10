<template>
  <div>
    <b-button v-b-modal.modal-1>Launch demo modal</b-button>
    <b-modal id="modal-1" no-fade title="Match columns"
             @ok="ok"
    >
      <b-form-group v-for="(col, index) in cols" :key="index"
                    :label="col"
                    label-cols="4"
                    label-cols-lg="2" label-for="input-sm"
                    label-size="sm">
        <b-form-select
          v-model="selected[index]"
          :options="options"
          class="mb-3">
        </b-form-select>
      </b-form-group>
    </b-modal>
  </div>
</template>

<script>
import tables from '@/util/databaseTables';

export default {
  name: 'ColumnSelector',
  props: {
    inputColumns: Array,
    table: String,
  },
  data() {
    return {
      cols: this.inputColumns,
      selected: new Array(this.inputColumns.length),
    };
  },
  computed: {
    options() {
      return tables[this.table].map((row) => ({
        text: row.label,
        value: row.key,
      }));
    },
  },
  mounted() {
    this.matchColumns();
  },
  methods: {
    ok() {
      console.log(this.selected);
    },
    matchColumns() {
      this.selected = this.cols.map((col) => {
        const matched = tables[this.table].find((el) => el.key === col);
        return matched ? matched.key : col;
      });
    },
  },
};
</script>

<style scoped>

</style>
