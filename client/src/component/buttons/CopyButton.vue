<template>
  <b-button v-clipboard:copy="target" v-clipboard:success="onCopy"
            class="mr-3">
    <b-icon aria-hidden="true" icon="trash"></b-icon>
    Копировать
  </b-button>
</template>

<script>

export default {
  name: 'CopyButton',
  props: {
    target: String,
  },
  methods: {
    onCopy() {
      this.$toasted.show('Скопировано в буфер');
    },
  },
};
</script>

<style scoped>

</style>
