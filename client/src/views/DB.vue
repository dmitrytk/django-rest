<template>
  <b-container>
    <div v-if="this.field">
      <h2 class="text-center my-3">
        {{ this.field.name }} {{ this.field.type }} месторождение
      </h2>
      <b-card class="mb-3">
        <b-nav class="my-0" pills>
          <b-nav-item :active="this.$route.path.includes('wells')" to="/db/wells">
            Скважины
          </b-nav-item>
          <b-nav-item :active="this.$route.path.includes('map')"
                      to="/db/map">Карта
          </b-nav-item>
          <b-nav-item :active="this.$route.path.includes('field')"
                      to="/db/field">Данные месторождения
          </b-nav-item>
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
  title: 'База данных',
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
      if (localStorage.getItem('lastFieldId')) {
        this.fetchField(localStorage.getItem('lastFieldId'));
        this.fetchWells(localStorage.getItem('lastFieldId'));
      } else {
        this.setSelectionVisible(true);
      }
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
      'fetchField',
      'setSelectionVisible',
    ]),
    ...mapActions('wells', [
      'fetchWells',
    ]),
  },
};
</script>

<style scoped>

</style>
