<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title v-if="field" primary-title>
        <div class="headline primary--text">{{ field.name }} месторождение
          <v-btn class="mr-3" color="primary" small @click="changeField">
            <v-icon>mdi-folder-open</v-icon>
          </v-btn>
        </div>

      </v-card-title>
      <v-row>
        <v-col lg="3">
          <WellList/>
        </v-col>
        <v-col lg="9"></v-col>
      </v-row>
      <FieldSelector/>
    </v-card>
  </v-container>
</template>

<script>

import FieldSelector from '@/components/FieldSelector.vue';
import { mapActions, mapGetters } from 'vuex';
import WellList from '@/components/WellList.vue';

export default {
  name: 'Database',
  components: { WellList, FieldSelector },
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
