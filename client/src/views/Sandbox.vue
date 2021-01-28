<template>
  <div>
    <b-container>
      <h2 class="text-center my-3">Sandbox</h2>
      <b-card>
        <b-form-file
          ref="file-input"
          v-model="file"
          class="mb-2"
          size="lg">
        </b-form-file>

        <b-table v-if="header && body"
                 ref="table"
                 :fields="header" :items="body"
                 head-variant="dark"
                 responsive
                 sticky-header>
        </b-table>

        <b-button class="mr-3" variant="primary" @click="calculate">Рассчитать</b-button>
        <b-button variant="danger" @click="clear">
          <b-icon aria-hidden="true" icon="trash"></b-icon>
          Очистить
        </b-button>
      </b-card>
    </b-container>
  </div>
</template>
<script>

import { calculateDeclineTable, parseData } from '../util/decline';
import { getTableData } from '../util/table';

export default {
  name: 'Sandbox',
  components: {},
  data() {
    return {
      file: null,
      inputData: null,
      result: null,
      header: null,
      body: null,
    };
  },
  methods: {
    calculate() {
      const reader = new FileReader();
      reader.readAsText(this.file, 'UTF-8');
      reader.onload = (evt) => {
        const rawData = evt.target.result;
        const parsedData = parseData(rawData);
        const { header, body } = calculateDeclineTable(parsedData);
        this.header = header.map((el) => ({
          label: el,
          key: el,
        }));
        this.body = getTableData(header, body);
      };
    },
    clear() {
      this.file = null;
      this.header = null;
      this.body = null;
    },
  },
};
</script>
