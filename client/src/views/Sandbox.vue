<template>
  <div>
    <b-container>
    </b-container>
  </div>
</template>

<script>
import getTableData from '@/util/table';

const mockData = `скважина\tx\ty
331R\t13566588.5\t6739251.165
335R\t13561534.8\t6734774.297
337R\t13566221.62\t6744041.206
340R\t13562965.11\t6743459.514
341R\t13564186.93\t6748381.851
342R\t13555210.76\t6741187.011
`;

export default {
  name: 'Sandbox',
  data() {
    return {};
  },
  mounted() {
    console.log(getTableData(mockData));
  },

};
</script>
