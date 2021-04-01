<template>
  <v-tab-item>
    <v-data-table v-if="content && content.length>0"
                  :headers="fields"
                  :items="content"
                  class="elevation-1"
    ></v-data-table>
  </v-tab-item>
</template>

<script>
import tables from '@/util/databaseTables';

export default {
  name: 'GenericTableTab',
  props: {
    tableName: String,
    parent: String,
  },
  data() {
    return {
      fields: tables[this.tableName],
    };
  },
  computed: {
    content() {
      return this.$store.getters[`${this.parent}/${this.tableName}`];
    },
  },
};
</script>

<style scoped>

</style>
