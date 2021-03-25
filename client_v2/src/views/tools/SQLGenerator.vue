<template>
  <v-container fluid>

    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">SQL Генератор</div>
      </v-card-title>

      <v-card-text>
        <v-row>
          <v-col lg="6">
            <label>Исходные данные</label>
            <v-textarea
              v-model="input"
              rows="15"
            ></v-textarea>
          </v-col>
          <v-col lg="6">
            <label>Результат</label>
            <v-textarea
              v-model="output"
              rows="15"
            ></v-textarea>
          </v-col>
        </v-row>
        <v-text-field v-model="table"
                      class="mr-2"
                      label="Таблица"
                      type="text"
        ></v-text-field>
        <v-row>
          <v-col md="2">
            <v-checkbox v-model="drop" class="mr-2" label="Drop">
            </v-checkbox>
          </v-col>
          <v-col md="2">
            <v-checkbox v-model="create" class="mr-2" label="Create">
            </v-checkbox>
          </v-col>
          <v-col md="2">
            <v-checkbox v-model="id" class="mr-2" label="Add id">
            </v-checkbox>
          </v-col>
        </v-row>
        <form inline>
          <v-btn :disabled="input.length===0"
                 class="mr-3"
                 variant="primary"
                 @click="generate">
            <v-icon icon="chevron-double-right"></v-icon>
            Генерировать SQL
          </v-btn>
        </form>

      </v-card-text>

    </v-card>
  </v-container>
</template>

<script>

import { csv } from '@/util/mock';
import generateSQL from '@/util/sql';

export default {
  name: 'SQLGenerator',
  title: 'SQL генератор',
  data() {
    return {
      input: csv,
      output: '',
      table: 'mytable',
      drop: true,
      create: true,
      id: true,
    };
  },
  methods: {
    generate() {
      this.output = generateSQL(
        this.input,
        this.table,
        this.drop,
        this.create,
        this.id,
      );
    },
    clear() {
      this.input = '';
      this.output = '';
    },
    onCopy() {
      this.$toasted.show('Скопировано в буфер');
    },
  },
};

</script>
