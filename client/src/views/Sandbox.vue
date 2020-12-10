<template>
  <b-container>
    <h1 class="text-center my-3">Sandbox</h1>
    <ColumnSelector :inputColumns="columns" table="wells"/>
  </b-container>
</template>

<script>

import ColumnSelector from '@/component/ColumnSelector.vue';

const localColumns = ['name', 'bottom', 'x'];

export default {
  name: 'Sandbox',
  components: { ColumnSelector },
  data() {
    return {
      columns: localColumns,
    };
  },
  mounted() {
  },
};
</script>

<style scoped>

</style>
