<template>
  <v-list v-if="wells && wells.length>0">
    <v-subheader>Скважины</v-subheader>
    <v-list-item-group
      v-model="selectedWell"
      color="primary">
      <v-list-item v-for="(well, index) in wells" :key="index" @click="selectWell(well)">
        <v-list-item-content>
          <v-list-item-title v-text="well.name"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>

    </v-list-item-group>
  </v-list>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'WellList',
  data() {
    return {
      selectedWell: null,
      hoveredWell: null,
    };
  },
  mounted() {
    if (this.well) {
      const wellIndex = this.wells.findIndex((w) => w.id === this.well.id);
      if (wellIndex !== -1) this.selectedWell = wellIndex;
    }
  },
  computed: {
    ...mapGetters('wells', [
      'wells',
      'well',
    ]),
  },
  methods: {
    ...mapActions('wells', [
      'fetchWell',
    ]),
    selectWell(well) {
      this.fetchWell(well.id);
    },
  },
};
</script>

<style scoped>

</style>
