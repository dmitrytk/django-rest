<template>
  <div>
    <b-table v-if="inclinometry && inclinometry.length>0" ref="table"
             :fields="fields" :items="inclinometry"
             head-variant="dark"
             responsive
             sticky-header>
    </b-table>
    <p v-else>Нет данных</p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import tables from '../../util/databaseTables';

export default {
  name: 'FieldInclinometryTable',
  data() {
    return {
      fields: tables.inclinometry,
    };
  },
  computed: {
    ...mapGetters('fields', [
      'inclinometry',
    ]),
  },
};
</script>

<style scoped>

</style>
