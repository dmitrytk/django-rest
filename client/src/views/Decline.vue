<template>
  <b-container>
    <h2 class="text-center my-3">Расчет понижений</h2>
    <b-card>
      <b-form-file
        ref="file-input"
        v-model="file"
        class="mb-3"
        drop-placeholder="Перетащите файл..."
        placeholder="Откройте или перетащите CSV файл..."
        size="lg">
      </b-form-file>

      <!--      <b-table :items="items" thead-class="hidden_header"/>-->

      <b-table v-if="header && body"
               ref="table"
               :fields="header" :items="body"
               head-variant="dark"
               responsive
               sticky-header>
      </b-table>

      <b-row>
        <b-col>
          <b-button class="mr-3" variant="primary" @click="calculate">
            <b-icon icon="chevron-double-right"></b-icon>
            Рассчитать
          </b-button>
          <ClearButton :callback="clear"/>
        </b-col>
        <b-col class="text-right">
          <b-button id="template" v-b-modal.modal-1>Шаблон</b-button>
          <b-modal id="modal-1" ok-only size="xl" title="Шаблон файла CSV">
            <b-table :items="items" responsive thead-class="hidden_header"/>
          </b-modal>
        </b-col>
      </b-row>

    </b-card>
  </b-container>
</template>

<script>

import ClearButton from '@/component/buttons/ClearButton.vue';
import { calculateDeclineTable, parseData } from '../util/decline';
import { getTableData } from '../util/table';

const template = [
  ['KM', 'A', '', '', '', '', '', ''],
  [80.25, 5.45],
  ['WELL', 'X', 'Y', 'R', '01.10.2020', '31.12.2020', '31.12.2021', '01.10.2022'],
  ['1067', '123123', '5353453', '0.07', '0', '700', '700', '700'],
  ['1068', '2342343', '234234', '0.073', '0', '550', '550', '500'],

];

export default {
  name: 'Decline',
  components: { ClearButton },
  data() {
    return {
      file: null,
      inputData: null,
      result: null,
      header: null,
      body: null,
      items: template,
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

<style>
.hidden_header {
  display: none;
}
</style>
