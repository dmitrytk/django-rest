<template>
  <wrapper>
    <v-dialog
      v-model="dialog"
      width="800"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          v-bind="attrs"
          v-on="on"
          color="red lighten-2"
          dark>
          <v-icon>mdi-table</v-icon>
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="headline grey lighten-2">
          Шаблон файла CSV
        </v-card-title>

        <v-card-text>
          <SimpleTable :body="template.slice(1)" :header="template[0]"/>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            class="mt-3"
            color="primary"
            text
            @click="close"
          >

            Закрыть
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </wrapper>
</template>

<script>
import SimpleTable from '@/components/SimpleTable.vue';
import { template } from '@/util/decline';

export default {
  name: 'DeclineTemplateDialog',
  components: { SimpleTable },
  data() {
    return {
      dialog: false,
      template,
    };
  },
  methods: {
    close() {
      const result = template.map((row) => row.join('\t')).join('\n');
      this.$copyText(result);
      this.dialog = false;
    },
  },
};
</script>

<style scoped>

</style>
