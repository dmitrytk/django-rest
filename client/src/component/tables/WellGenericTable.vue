<template>
  <div>
    <b-table v-if="data &&
    data.length>0" ref="table"
             :fields="fields" :items="data"
             head-variant="dark"
             responsive
             sticky-header>
    </b-table>
    <p v-else>No data</p>
    <b-button variant="danger" @click="log">Delete</b-button>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import tables from '../../util/databaseTables';

export default {
  name: 'WellGenericTable',
  props: ['tableName'],
  data() {
    return {
      fields: tables[this.tableName],
    };
  },
  computed: {
    ...mapGetters('wells', [
      'mer',
      'inclinometry',
      'rates',
    ]),
    data() {
      return this.$store.getters[`wells/${this.tableName}`];
    },
  },
  methods: {
    log() {
      console.log('Delete');
    },
  },
};
</script>

<style scoped>

</style>
