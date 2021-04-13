<template>
  <v-icon
    color="danger"
    icon="trash-fill"
    @click="deleteWell"></v-icon>
</template>

<script>
import {mapGetters} from 'vuex';

export default {
  name: 'WellDeleteIcon',
  props: ['wellId'],
  computed: {
    ...mapGetters('wells', ['well']),
  },
  methods: {
    async deleteWell() {
      this.$bvModal.msgBoxConfirm('Вы уверены что хотите удалить скважину?', {
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
            const result = await this.$store.dispatch('wells/deleteWell', this.wellId);
            console.log(result.status);
            if (result) {
              this.$toasted.show('Скважина удалена');
              await this.$store.dispatch('wells/fetchWells', this.well.field);
              await this.$store.dispatch('fields/fetchField', this.well.field);
              this.$store.commit('wells/setWell', null);
            }
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
