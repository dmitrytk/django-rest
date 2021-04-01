<template>
  <v-btn v-clipboard:copy="target" v-clipboard:success="onCopy" class="mr-3">
    <v-icon>mdi-clipboard-multiple-outline</v-icon>
    Копировать
  </v-btn>
</template>

<script>

export default {
  name: 'CopyButton',
  props: {
    target: String,
  },
  methods: {
    onCopy() {
      console.log('Copy');
    },
  },
};
</script>

<style scoped>

</style>
