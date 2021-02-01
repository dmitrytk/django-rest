<template>
  <b-container>
    <h2 class="text-center my-3">Расчет понижений</h2>
    <b-overlay :show="showOverlay" rounded="sm">
      <b-card>
        <b-form-file
          ref="file-input"
          v-model="file"
          class="mb-3"
          drop-placeholder="Перетащите файл..."
          placeholder="Откройте или перетащите CSV файл..."
          size="lg">
        </b-form-file>

        <p v-if="data" class="mb-3 font-weight-bold">
          KM = {{ data.km }}; A = {{ data.a }}; {{ data.wells.length }} скважин
        </p>

        <!--      TABLE      -->
        <b-table v-if="header && body"
                 ref="table"
                 :fields="header" :items="body"
                 head-variant="dark"
                 responsive
                 sticky-header>
        </b-table>

        <!--      CHECKBOX      -->
        <b-form-checkbox
          v-model="selected"
          class="mb-3">
          Сетка
        </b-form-checkbox>

        <!--      GRID PARAMS      -->
        <b-row v-if="selected">
          <b-col>
            <b-form-group>
              <label>Шаг сетки, м</label>
              <b-form-input
                v-model="step"
                type="number">
              </b-form-input>
            </b-form-group>
          </b-col>

          <b-col>
            <b-form-group>
              <label>Запас сетки, м</label>
              <b-form-input
                v-model="margin"
                type="number">
              </b-form-input>
            </b-form-group>
          </b-col>

          <b-col>
            <b-form-group>
              <label>Дополнительное понижение, м</label>
              <b-form-input
                v-model="additionalDrawdown"
                type="number">
              </b-form-input>
            </b-form-group>
          </b-col>
        </b-row>

        <!--      BUTTONS      -->
        <b-row>
          <b-col>
            <b-button :disabled="!data" class="mr-3" variant="primary" @click="calculate">
              <b-icon icon="chevron-double-right"></b-icon>
              Рассчитать
            </b-button>
            <ClearButton :callback="clear"/>
          </b-col>
          <b-col class="text-right">
            <b-button id="template" v-b-modal.modal-1 @click="copyTemplate">Шаблон</b-button>
            <b-modal
              id="modal-1"
              ok-only
              size="xl"
              title="Шаблон файла CSV"
              @ok="handleOk">
              <b-table :items="items" responsive thead-class="hidden_header"/>
            </b-modal>
          </b-col>
        </b-row>

      </b-card>
    </b-overlay>

  </b-container>
</template>

<script>

import ClearButton from '@/component/buttons/ClearButton.vue';
import {
  calculateDeclineTable, calculateGrid, parseData, template, writeGrid,
} from '../util/decline';
import { getTableData } from '../util/table';

export default {
  name: 'Decline',
  components: { ClearButton },
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
      selected: null,
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
      this.showOverlay = true;
      setTimeout(() => {
        const { header, body } = calculateDeclineTable(this.data);
        this.header = header;
        this.body = getTableData(header, body);
        if (this.selected) {
          this.grid = calculateGrid(this.data, this.step, this.margin, this.additionalDrawdown);
          writeGrid(this.grid);
        }
        this.showOverlay = false;
      }, 50);
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
