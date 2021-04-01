<template>
  <v-dialog
    v-model="dialog"
    max-width="290"
    persistent
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        v-bind="attrs"
        v-on="on"
        class="mt-3"
        color="error"
        dark
      >
        Удалить
      </v-btn>
    </template>
    <v-card>
      <v-card-title class="headline">
        Удалить ресурс?
      </v-card-title>
      <v-card-actions>
        <v-btn
          color="green darken-1"
          text
          @click="dialog = false"
        >
          Отмена
        </v-btn>
        <v-btn
          color="error darken-1"
          text
          @click="deleteResource"
        >
          Удалить
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
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
  data() {
    return {
      dialog: false,
    };
  },
  computed: {
    ...mapGetters('fields', ['field']),
    ...mapGetters('wells', ['well']),
  },
  methods: {
    async deleteResource() {
      try {
        this.dialog = false;
        await this.$store.dispatch(`${this.parent}/delete${capitalize(this.resource)}`, this.parentId);
        this.$store.dispatch(`fields/fetch${capitalize(this.resource)}`, this.field.id);
        this.$store.dispatch(`wells/fetch${capitalize(this.resource)}`, this.well.id);
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>

<style scoped>

</style>
