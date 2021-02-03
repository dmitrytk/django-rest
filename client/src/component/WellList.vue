<template>

  <b-list-group>
    <b-list-group-item v-for="well in orderedWells"
                       :key="well.name"
                       :active="well.id===selectedWellId"
                       @click="selectWell(well.id)">
      <b-row>
        <b-col sm="10">
          {{ well.name }}
          <template v-if="well.type">/ {{ well.type.charAt(0) }}</template>
        </b-col>
        <b-col sm="1">
          <WellDeleteIcon
            :hidden="!(well.id===selectedWellId)"
            :wellId="well.id"/>
          <!--          <b-icon-->
          <!--            :hidden="!(well.id===selectedWellId)"-->
          <!--            class="clickable text-right"-->
          <!--            icon="trash-fill"-->
          <!--            variant="danger"-->
          <!--            @click="deleteWell(well.id)"></b-icon>-->
        </b-col>
      </b-row>

    </b-list-group-item>
  </b-list-group>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import WellDeleteIcon from './icons/WellDeleteIcon.vue';

export default {
  name: 'WellList',
  components: { WellDeleteIcon },
  data() {
    return {
      selectedWellId: null,
      hoveredWell: null,
    };
  },
  mounted() {
    if (this.well) {
      const well = this.wells.find((w) => w.id === this.well.id);
      if (well) this.selectedWellId = well.id;
    }
  },
  computed: {
    ...mapGetters('wells', [
      'wells',
      'well',
    ]),
    orderedWells() {
      // eslint-disable-next-line vue/no-side-effects-in-computed-properties
      return this.wells.sort((a, b) => (a.name > b.name ? 1 : -1));
    },
  },
  methods: {
    ...mapActions('wells', [
      'fetchWell',
    ]),
    selectWell(wellId) {
      this.fetchWell(wellId);
      this.selectedWellId = wellId;
    },
    deleteWell(id) {
      console.log(id);
    },
  },
};
</script>

<style scoped>

</style>
