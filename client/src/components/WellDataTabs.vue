<template>
  <div>
    <v-tabs v-model="tab">
      <v-tab>
        Данные
      </v-tab>
      <v-tab>
        Инклинометрия
      </v-tab>
      <v-tab>
        МЭР
      </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        <WellForm/>
      </v-tab-item>
      <v-tab-item>
        <v-data-table v-if="inclinometry && inclinometry.length>0"
                      :headers="incHeader"
                      :items="inclinometry"
                      class="elevation-1"
        ></v-data-table>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import tables from '@/util/databaseTables';
import WellForm from '@/components/forms/WellForm.vue';

export default {
  name: 'WellDataTabs',
  components: { WellForm },
  data() {
    return {
      tab: null,
      incHeader: tables.inclinometry,
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
