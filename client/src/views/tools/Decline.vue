<template>
  <v-container>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Расчет понижений</div>
      </v-card-title>
      <v-file-input
        ref="file-input"
        v-model="file"
        accept=".csv"
        class="mb-3"
        placeholder="Откройте CSV файл..."
        size="lg">
      </v-file-input>

      <p v-if="data" class="mb-3 font-weight-bold">
        KM = {{ data.km }}; A = {{ data.a }}; {{ data.wells.length }} скважин
      </p>

      <SimpleTable v-if="header && body" :body="body" :header="header"/>

      <!--      CHECKBOX      -->
      <v-checkbox
        v-model="generateGrid" label="Сетка">
        Сетка
      </v-checkbox>

      <!--      GRID PARAMS      -->
      <v-row v-if="generateGrid">
        <v-col md="4">
          <v-text-field
            v-model="step"
            label="Шаг сетки, м"
            type="number">
          </v-text-field>
        </v-col>

        <v-col md="4">
          <v-text-field
            v-model="margin"
            label="Запас сетки, м"
            type="number">
          </v-text-field>
        </v-col>

        <v-col md="4">
          <v-text-field
            v-model="additionalDrawdown"
            label="Доп. понижение, м"
            type="number">
          </v-text-field>
        </v-col>
      </v-row>

      <!--      BUTTONS      -->
      <v-row>
        <v-col>
          <v-btn :disabled="!data" class="mr-3" variant="primary" @click="calculate">
            <v-icon>mdi-play</v-icon>
            Рассчитать
          </v-btn>
          <ClearButton :callback="clear"/>
        </v-col>
        <v-col class="text-right">
          <DeclineTemplateDialog/>
        </v-col>
      </v-row>

    </v-card>
  </v-container>

</template>

<script>

import ClearButton from '@/components/buttons/ClearButton.vue';
import {
  calculateDeclineTable, calculateGrid, parseData, template, writeGrid,
} from '@/util/decline';
import { getTableData } from '@/util/table';
import SimpleTable from '@/components/SimpleTable.vue';
import DeclineTemplateDialog from '@/components/DeclineTemplateDialog.vue';

export default {
  name: 'Decline',
  title: 'Расчет понижений',
  components: { DeclineTemplateDialog, SimpleTable, ClearButton },
  data() {
    return {
      file: null,
      data: null,
      result: null,
      header: null,
      body: null,
      grid: null,
      showOverlay: false,
      showMap: false,
      items: template,
      step: 200,
      margin: 3000,
      additionalDrawdown: 0,
      generateGrid: null,
    };
  },
  watch: {
    file() {
      if (this.file) {
        const reader = new FileReader();
        reader.readAsText(this.file, 'UTF-8');
        reader.onload = (evt) => {
          const rawData = evt.target.result;
          this.data = parseData(rawData);
        };
      }
    },
  },
  methods: {
    calculate() {
      console.log(this.data);
      this.showOverlay = true;
      setTimeout(() => {
        const { header, body } = calculateDeclineTable(this.data);
        this.header = header;
        this.body = getTableData(header, body);
        if (this.generateGrid) {
          this.grid = calculateGrid(this.data, this.step, this.margin, this.additionalDrawdown);
          writeGrid(this.grid);
        }
        this.showOverlay = false;
      }, 25);
    },
    clear() {
      this.data = null;
      this.file = null;
      this.header = null;
      this.body = null;
      this.grid = null;
      this.showMap = false;
    },
    copyTemplate() {
      const result = template.map((row) => row.join('\t')).join('\n');
      this.$copyText(result);
    },
    handleOk() {
      this.$toasted.show('Скопировано в буфер');
    },
  },
};
</script>

<style>
.hidden_header {
  display: none;
}
</style>
