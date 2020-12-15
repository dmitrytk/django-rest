<template>
  <div>
    <b-table v-if="inclinometry && inclinometry.length>0" ref="table"
             :fields="fields" :items="inclinometry"
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
  name: 'InclinometryTable',
  data() {
    return {
      fields: tables.inclinometry,
    };
  },
  computed: {
    ...mapGetters('wells', [
      'inclinometry',
    ]),
  },
};
</script>

<style scoped>

</style>
