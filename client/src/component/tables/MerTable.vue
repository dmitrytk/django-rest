<template>
  <div>
    <b-table v-if="mer && mer.length>0" ref="table"
             :fields="fields" :items="mer"
             head-variant="dark"
             responsive
             sticky-header>
    </b-table>
    <p v-else>No data</p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import tables from '../../util/databaseTables';

export default {
  name: 'MerTable',
  data() {
    return {
      fields: tables.mer,
    };
  },
  computed: {
    ...mapGetters('wells', [
      'mer',
    ]),
  },
};
</script>

<style scoped>

</style>
