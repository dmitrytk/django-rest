<template>
  <v-row v-if="wells && wells.length>0">
    <v-col class="mx-3 pr-0" lg="3">
      <v-card class="pa-3">
        <WellList/>
      </v-card>
    </v-col>
    <v-col class="mr-3">
      <v-card class="pa-3">
        <WellDataTabs/>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { mapGetters } from 'vuex';
import WellList from '@/components/WellList.vue';
import WellDataTabs from '@/components/WellDataTabs.vue';

export default {
  name: 'Wells',
  components: { WellDataTabs, WellList },
  computed: {
    ...mapGetters('wells', [
      'wells',
      'well',
    ]),
  },
};
</script>

<style scoped>

</style>
