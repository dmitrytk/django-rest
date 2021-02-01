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

    <div v-if="data && data.length">
      <CopyTableButton :body="data" :header="fields"/>
      <DeleteButton
        :parentId="well.id"
        :resource="tableName"
        parent="wells"></DeleteButton>
    </div>
  </div>

</template>

<script>
import { mapGetters } from 'vuex';
import CopyTableButton from '@/component/buttons/CopyTableButton.vue';
import tables from '@/util/databaseTables';
import DeleteButton from '@/component/buttons/DeleteButton.vue';

export default {
  name: 'WellGenericTable',
  components: { CopyTableButton, DeleteButton },
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
};
</script>

<style scoped>

</style>
