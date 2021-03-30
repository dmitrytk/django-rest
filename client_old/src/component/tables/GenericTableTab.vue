<template>
  <b-tab :title="`${data && data.length?`${title} (${data.length})`:title}`">
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
        :parent="parent"
        :parentId="parentId"
        :resource="tableName"></DeleteButton>
    </div>
  </b-tab>

</template>

<script>
import CopyTableButton from '@/component/buttons/CopyTableButton.vue';
import tables from '@/util/databaseTables';
import DeleteButton from '@/component/buttons/DeleteButton.vue';

export default {
  name: 'WellGenericTableTab',
  components: { CopyTableButton, DeleteButton },
  props: ['parent', 'parentId', 'title', 'tableName'],
  data() {
    return {
      fields: tables[this.tableName],
    };
  },
  computed: {
    data() {
      return this.$store.getters[`${this.parent}/${this.tableName}`];
    },
  },
};
</script>

<style scoped>

</style>
