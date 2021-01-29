<template>
  <b-button class="mr-3" variant="danger" @click="callback">
    <b-icon aria-hidden="true" icon="trash"></b-icon>
    Очистить
  </b-button>
</template>

<script>
export default {
  name: 'ClearButton',
  props: {
    callback: Function,
  },
};
</script>

<style scoped>

</style>
