<template>
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
        <WellForm/>
      </v-tab-item>
      <GenericTableTab v-for="(table, index) in tables"
                       :key="index"
                       :parentId="well.id"
                       :tableName="table.value"
                       parent="wells"/>
    </v-tabs-items>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import WellForm from '@/components/forms/WellForm.vue';
import GenericTableTab from './GenericTableTab.vue';

export default {
  name: 'WellDataTabs',
  components: { GenericTableTab, WellForm },
  data() {
    return {
      tab: null,
      tables: [
        { text: 'Инклинометрия', value: 'inclinometry' },
        { text: 'Режимы', value: 'rates' },
        { text: 'МЭР', value: 'mer' },
        { text: 'Пласты', value: 'horizons' },
      ],
    };
  },
  computed: {
    ...mapGetters('wells', [
      'wells',
      'well',
      'inclinometry',
    ]),
  },
};
</script>

<style scoped>

</style>
