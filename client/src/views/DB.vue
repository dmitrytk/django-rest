<template>
  <b-container>
    <h1 v-if="this.field" class="text-center my-3">
      {{ this.field.name }} месторождение
      <b-icon class="clickable" icon="arrow-repeat" @click="changeDB()"></b-icon>
    </h1>
    <b-row v-if="this.wells && this.wells.length>0">
      <b-col lg="3">
        <b-card>
          <h4 class="text-center">Скважины</h4>
          <WellList/>
        </b-card>
      </b-col>

      <b-col lg="9">

        <b-card v-if="well">
          <b-tabs content-class="mt-3">
            <b-tab active title="Основные данные">
              <WellForm/>
            </b-tab>
            <b-tab title="Инклинометрия">
              <InclinometryTable/>
            </b-tab>
            <b-tab title="МЭР">
              <MerTable/>
            </b-tab>
            <b-tab title="Пласты"></b-tab>
          </b-tabs>

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
import InclinometryTable from '@/component/tables/InclinometryTable.vue';
import MerTable from '@/component/tables/MerTable.vue';

export default {
  name: 'DB',
  components: {
    MerTable,
    InclinometryTable,
    WellList,
    FieldSelector,
    WellForm,
  },
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
      console.log('Change Database');
    },

  },
};
</script>

<style scoped>

</style>
