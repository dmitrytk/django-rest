<template>
  <div>
    <b-table v-if="data &&
    data.length>0" ref="table"
             :fields="fields" :items="data"
             head-variant="dark"
             responsive
             sticky-header>
    </b-table>
    <p v-else>Нет данных</p>
    <DeleteButton v-if="data && data.length"
                  :parentId="well.id"
                  :resource="tableName"
                  parent="wells"></DeleteButton>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import tables from '../../util/databaseTables';
import DeleteButton from '../DeleteButton.vue';

export default {
  name: 'WellGenericTable',
  components: { DeleteButton },
  props: ['tableName'],
  data() {
    return {
      fields: tables[this.tableName],
    };
  },
  computed: {
    ...mapGetters('wells', [
      'well',
      'mer',
      'inclinometry',
      'rates',
    ]),
    data() {
      return this.$store.getters[`wells/${this.tableName}`];
    },
  },
  methods: {},
};
</script>

<style scoped>

</style>
