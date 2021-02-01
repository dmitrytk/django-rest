<template>
  <b-button class="mr-3"
            @click="copy">
    <b-icon aria-hidden="true" icon="clipboard-plus"></b-icon>
    Копировать
  </b-button>
</template>

<script>

import { tableToString } from '../../util/table';

export default {
  name: 'CopyTableButton',
  props: {
    header: Array,
    body: Array,
  },
  methods: {
    copy() {
      const result = tableToString(this.header, this.body);
      this.$copyText(result);
      this.$toasted.show('Скопировано в буфер');
    },
  },
};
</script>

<style scoped>

</style>
