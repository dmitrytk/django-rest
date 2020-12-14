<template>
  <b-list-group>
    <b-list-group-item
      v-for="well in this.wells"
      :key="well.id"
      :active="well.id===selectedWellId"
      @click="selectWell(well.id)"
    >
      {{ well.name }}
    </b-list-group-item>
  </b-list-group>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'WellList',
  data() {
    return {
      selectedWellId: null,
    };
  },
  computed: {
    ...mapGetters('wells', [
      'wells',
    ]),
  },
  methods: {
    ...mapActions('wells', [
      'fetchWell',
    ]),
    selectWell(wellId) {
      this.fetchWell(wellId);
      this.selectedWellId = wellId;
    },
  },
};
</script>

<style scoped>

</style>
