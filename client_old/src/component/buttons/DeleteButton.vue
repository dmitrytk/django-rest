<template>
  <b-button variant="danger" @click="deleteResource">
    <b-icon aria-hidden="true" icon="trash"></b-icon>
    Удалить
  </b-button>
</template>

<script>
import { mapGetters } from 'vuex';
import capitalize from '../../util/string';

export default {
  name: 'DeleteButton',
  props: {
    parent: String,
    parentId: Number,
    resource: String,
  },
  computed: {
    ...mapGetters('fields', ['field']),
    ...mapGetters('wells', ['well']),
  },
  methods: {
    async deleteResource() {
      this.$bvModal.msgBoxConfirm('Вы уверены что хотите удалить данные?', {
        size: 'sm',
        buttonSize: 'sm',
        okVariant: 'danger',
        okTitle: 'Удалить',
        cancelTitle: 'Отмена',
        footerClass: 'p-2',
        hideHeaderClose: false,
        centered: true,
      })
        .then(async (value) => {
          if (value) {
            await this.$store.dispatch(`${this.parent}/delete${capitalize(this.resource)}`, this.parentId);
            this.$toasted.show('Данные удалены');
            this.$store.dispatch(`fields/fetch${capitalize(this.resource)}`, this.field.id);
            this.$store.dispatch(`wells/fetch${capitalize(this.resource)}`, this.well.id);
          }
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
