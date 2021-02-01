<template>
  <b-button variant="danger" @click="deleteResource">
    <b-icon aria-hidden="true" icon="trash"></b-icon>
    Удалить
  </b-button>
</template>

<script>
import capitalize from '../../util/string';

export default {
  name: 'DeleteButton',
  props: {
    parent: String,
    parentId: Number,
    resource: String,
  },
  methods: {
    deleteResource() {
      this.$bvModal.msgBoxConfirm('Вы уверены что хотите удалить ресурс?', {
        size: 'sm',
        buttonSize: 'sm',
        okVariant: 'danger',
        okTitle: 'Удалить',
        cancelTitle: 'Отмена',
        footerClass: 'p-2',
        hideHeaderClose: false,
        centered: true,
      })
        .then((value) => {
          if (value) {
            return this.$store.dispatch(`${this.parent}/delete${capitalize(this.resource)}`, this.parentId);
          }
          return 0;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>

</style>
