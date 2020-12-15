<template>
  <b-container>
    <div v-if="this.field">
      <h1 class="text-center my-3">
        {{ this.field.name }} месторождение
        <b-icon class="clickable" icon="arrow-repeat" @click="changeDB()"></b-icon>
      </h1>
      <b-card class="mb-3">
        <b-nav>
          <b-nav-item active to="/db/wells">Wells</b-nav-item>
          <b-nav-item to="/db/map">Map</b-nav-item>
          <b-nav-item to="/db/field">Field data</b-nav-item>
        </b-nav>
      </b-card>

      <router-view/>
    </div>
    <FieldSelector/>
  </b-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import FieldSelector from '@/component/FieldSelector.vue';

export default {
  name: 'DB',
  components: {
    FieldSelector,
  },
  data() {
    return {
      loading: false,
    };
  },
  mounted() {
    if (!this.field) {
      this.setSelectionVisible(true);
    }
  },
  computed: {
    ...mapGetters('fields', [
      'field',
      'fields',
      'fieldLoading',
      'fieldsLoading',
      'selectionVisible',
    ]),
    ...mapGetters('wells', [
      'well',
      'wells',
      'wellLoading',
      'wellsLoading',
    ]),
  },
  methods: {
    ...mapActions('fields', [
      'fetchFields',
      'setSelectionVisible',
    ]),
    changeDB() {
      console.log(this.selectionVisible);
      this.setSelectionVisible(true);
    },

  },
};
</script>

<style scoped>

</style>
