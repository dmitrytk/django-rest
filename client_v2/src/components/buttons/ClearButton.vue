<template>
  <v-btn class="mr-3" color="error" @click="callback">
    <v-icon>mdi-delete</v-icon>
    Очистить
  </v-btn>
</template>

<script>
export default {
  name: 'ClearButton',
  props: {
    callback: Function,
  },
  methods: {},
};
</script>

<style scoped>

</style>
