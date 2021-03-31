<template>
  <v-container fluid>
    <FieldSelector/>

    <v-card class="ma-3 pa-3">
      <v-card-title v-if="field" primary-title>
        <div class="headline primary--text">{{ field.name }} месторождение
          <v-btn class="mr-3" color="primary" small @click="changeField">
            <v-icon>mdi-folder-open</v-icon>
          </v-btn>
        </div>
      </v-card-title>
    </v-card>

    <v-row>
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

  </v-container>
</template>

<script>

import FieldSelector from '@/components/FieldSelector.vue';
import { mapActions, mapGetters } from 'vuex';
import WellList from '@/components/WellList.vue';
import WellDataTabs from '@/components/WellDataTabs.vue';

export default {
  name: 'Database',
  components: { WellDataTabs, WellList, FieldSelector },
  data() {
    return {};
  },
  mounted() {
    if (!this.field) {
      this.setSelectionVisible(true);
    }
  },
  computed: {
    ...mapGetters('fields', [
      'field',
      'fields',
      'selectionVisible',
    ]),
  },
  methods: {
    ...mapActions('fields', [
      'setSelectionVisible',

    ]),
    changeField() {
      this.setSelectionVisible(true);
    },
  },
};
</script>

<style scoped>

</style>
