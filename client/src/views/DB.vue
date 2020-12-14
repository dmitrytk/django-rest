<template>
  <b-container>
    <h1 v-if="this.field" class="text-center my-3">
      {{ this.field.name }} месторождение
    </h1>
    <b-row v-if="this.wells && this.wells.length>0">
      <b-col lg="3">
        <b-card>
          <WellList/>
        </b-card>
      </b-col>

      <b-col lg="9">
        <b-card>
          <WellForm/>
        </b-card>
      </b-col>
    </b-row>

    <FieldSelector/>
  </b-container>
</template>

<script>
import WellForm from '@/component/form/WellForm.vue';
import { mapActions, mapGetters } from 'vuex';
import FieldSelector from '@/component/FieldSelector.vue';
import WellList from '@/component/WellList.vue';

export default {
  name: 'DB',
  components: { WellList, FieldSelector, WellForm },
  data() {
    return {
      loading: false,
    };
  },
  mounted() {

  },
  computed: {
    ...mapGetters('fields', [
      'field',
      'fields',
      'fieldLoading',
      'fieldsLoading',
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
    ]),
    changeDB() {

    },

  },
};
</script>

<style scoped>

</style>
