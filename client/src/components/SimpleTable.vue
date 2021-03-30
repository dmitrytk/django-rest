<template>
  <v-simple-table height="500px">
    <template v-slot:default>
      <thead>
      <tr>
        <th v-for="(col,index) in header" :key="index" class="text-left">
          {{ col }}
        </th>
      </tr>
      </thead>
      <tbody>
      <tr
        v-for="(row, j) in body"
        :key="j">
        <td v-for="(cell, k) in row" :key="k">
          {{ cell }}
        </td>
      </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
export default {
  name: 'SimpleTable',
  props: {
    header: Array,
    body: Array,
  },
};
</script>

<style scoped>

</style>
