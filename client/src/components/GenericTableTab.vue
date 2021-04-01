<template>
  <v-tab-item>
    <div v-if="content && content.length>0">
      <v-data-table
        :headers="fields"
        :items="content"
        class="elevation-1"
      ></v-data-table>
      <DeleteButton
        :parent="parent"
        :parentId="parentId"
        :resource="tableName"></DeleteButton>
    </div>
  </v-tab-item>
</template>

<script>
import tables from '@/util/databaseTables';
import DeleteButton from '@/components/buttons/DeleteButton.vue';

export default {
  name: 'GenericTableTab',
  components: { DeleteButton },
  props: {
    tableName: String,
    parent: String,
    parentId: Number || null,
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
