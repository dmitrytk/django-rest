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
        <v-row justify="start">
          <v-col md="4">
            <v-text-field v-model="table"
                          :rules="tableNameRules"
                          class="mr-2"
                          label="Таблица"
                          type="text"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row justify="start">
          <v-col md="2">
            <v-checkbox v-model="drop" class="mr-3" label="Drop">
            </v-checkbox>
          </v-col>
          <v-col md="2">
            <v-checkbox v-model="create" class="mr-3" label="Create">
            </v-checkbox>
          </v-col>
          <v-col md="2">
            <v-checkbox v-model="id" class="mr-3" label="Add id">
            </v-checkbox>
          </v-col>
        </v-row>

        <div>
          <v-btn :disabled="input.length===0"
                 class="mr-3 mt-3"
                 color="primary"
                 @click="generate">
            <v-icon>mdi-play</v-icon>
            Генерировать SQL
          </v-btn>
          <CopyButton :target="output" class="mt-3"/>
          <ClearButton :callback="clear" class="mt-3"/>
        </div>

      </v-card-text>

    </v-card>
  </v-container>
</template>

<script>

import { csv } from '@/util/mock';
import generateSQL from '@/util/sql';
import ClearButton from '@/components/buttons/ClearButton.vue';
import CopyButton from '@/components/buttons/CopyButton.vue';

export default {
  name: 'SQLGenerator',
  components: { CopyButton, ClearButton },
  title: 'SQL генератор',
  data() {
    return {
      input: csv,
      output: '',
      table: 'mytable',
      drop: true,
      create: true,
      id: true,
      tableNameRules: [
        (v) => !!v || 'Table name is required',
        (v) => v.length <= 50 || 'Table Name must be less than 50 characters',
      ],
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
  },
};

</script>
