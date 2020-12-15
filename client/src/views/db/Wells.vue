<template>
  <div>
    <b-row v-if="this.wells && this.wells.length>0">
      <b-col lg="3">
        <b-card>
          <h4 class="text-center">Wells</h4>
          <WellList/>
        </b-card>
      </b-col>
      <b-col lg="9">
        <b-card v-if="well">
          <b-tabs content-class="mt-3">
            <b-tab active title="Well data">
              <WellForm/>
            </b-tab>
            <b-tab title="Inclinometry">
              <WellGenericTable tableName="inclinometry"/>
            </b-tab>
            <b-tab title="MER">
              <WellGenericTable tableName="mer"/>
            </b-tab>
            <b-tab title="Zones"></b-tab>
          </b-tabs>
        </b-card>
      </b-col>
    </b-row>
    <h3 v-else class="text-center">No wells</h3>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import WellList from '@/component/WellList.vue';
import WellForm from '@/component/form/WellForm.vue';
import WellGenericTable from '@/component/tables/WellGenericTable.vue';

export default {
  name: 'Wells',
  components: {
    WellGenericTable,
    WellList,
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
