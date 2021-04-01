<template>
  <v-card v-if="field" class="ma-3  pa-3">
    <div>
      <v-tabs v-model="tab">
        <v-tab>
          Данные
        </v-tab>
        <v-tab v-for="(table, index) in tables" :key="index">
          {{ table.text }}
        </v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab">
        <v-tab-item>
          <FieldForm/>
        </v-tab-item>
        <GenericTableTab v-for="(table, index) in tables"
                         :key="index"
                         :parentId="field.id"
                         :tableName="table.value"
                         parent="fields"/>

      </v-tabs-items>
    </div>
  </v-card>
</template>

<script>
import FieldForm from '@/components/forms/FieldForm.vue';
import GenericTableTab from '@/components/GenericTableTab.vue';
import { mapGetters } from 'vuex';

export default {
  name: 'Field',
  components: { GenericTableTab, FieldForm },
  data() {
    return {
      tab: null,
      tables: [
        { text: 'Инклинометрия', value: 'inclinometry' },
        { text: 'Режимы', value: 'rates' },
        { text: 'МЭР', value: 'mer' },
        { text: 'Пласты', value: 'zones' },
      ],
    };
  },
  computed: {
    ...mapGetters('fields', [
      'field',
    ]),
  },
};
</script>

<style scoped>

</style>
