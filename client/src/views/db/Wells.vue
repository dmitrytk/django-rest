<template>
  <v-row v-if="wells && wells.length>0">
    <v-col class="mx-3 pr-0" lg="3">
      <v-card class="pa-3">
        <WellList/>
      </v-card>
    </v-col>
    <v-col v-if="well" class="mr-3">
      <v-card class="pa-3">
        <WellDataTabs/>
      </v-card>
    </v-col>
  </v-row>
  <v-container v-else fluid>
    <v-card class="pa-3">
      <v-card-title>Нет скважин</v-card-title>
      <v-card-actions>
        <v-btn
          to="/main/import"
        >
          Загрузить
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import WellList from '@/components/WellList.vue';
import WellDataTabs from '@/components/WellDataTabs.vue';

export default {
  name: 'Wells',
  components: { WellDataTabs, WellList },
  mounted() {
    if (!this.wells) this.checkCurrentWells();
  },
  computed: {
    ...mapGetters('wells', [
      'wells',
      'well',
    ]),
  },
  methods: {
    ...mapActions('wells', [
      'checkCurrentWells',
    ]),
  },

};
</script>

<style scoped>

</style>
