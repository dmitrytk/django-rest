<template>
  <b-button variant="danger" @click="deleteResource">Удалить</b-button>
</template>

<script>
export default {
  name: 'DeleteButton',
  props: {
    parent: String,
    parentId: Number,
    resource: String,
  },
  methods: {
    deleteResource() {
      console.log(`/${this.parent}/${this.parentId}/${this.resource}/`);
    },
  },
};
</script>

<style scoped>

</style>
