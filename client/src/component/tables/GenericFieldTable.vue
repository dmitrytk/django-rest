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
        :parentId="field.id"
        :resource="tableName"
        parent="fields"></DeleteButton>
    </div>
  </div>

</template>

<script>
import CopyTableButton from '@/component/buttons/CopyTableButton.vue';
import tables from '@/util/databaseTables';
import DeleteButton from '@/component/buttons/DeleteButton.vue';
import { mapGetters } from 'vuex';

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
    ...mapGetters('fields', [
      'field',
      'mer',
      'inclinometry',
      'rates',
      'zones',
      'coordinates',
    ]),
    data() {
      return this.$store.getters[`fields/${this.tableName}`];
    },
  },
};
</script>

<style scoped>

</style>
