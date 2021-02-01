<template>
  <b-tab title="Диаграммы">
    <WellMerChart v-if="this.mer && this.mer.length>0"
                  id="merChart" :data="this.mer"/>
    <WellRateChart v-if="this.rates && this.rates.length>0"
                   id="ratesChart" :data="this.rates"
                   class="mb-3"/>
    <p v-else>Нет данных</p>
  </b-tab>
</template>

<script>
import { mapGetters } from 'vuex';
import WellMerChart from './charts/WellMerChart';
import WellRateChart from './charts/WellRateChart';

export default {
  name: 'ChartTab',
  components: {
    WellRateChart,
    WellMerChart,
  },
  data() {
    return {};
  },
  mounted() {
  },
  computed: {
    ...mapGetters('wells', [
      'well',
      'mer',
      'rates',
    ]),
  },
  methods: {
    log() {
      console.log('clicked');
    },
  },
};
</script>

<style scoped>

</style>
