<template>
  <div>
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
            <b-tab active title="Данные скважины">
              <WellForm/>
            </b-tab>
            <b-tab title="Инклинометрия">
              <WellGenericTable tableName="inclinometry"/>
            </b-tab>
            <b-tab title="МЭР">
              <WellGenericTable tableName="mer"/>
            </b-tab>
            <b-tab title="Пласты">
              <WellGenericTable tableName="zones"/>
            </b-tab>
          </b-tabs>
        </b-card>
      </b-col>
    </b-row>
    <h4 v-else class="text-center">Нет скважин
      <ImportButton/>
    </h4>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import WellList from '@/component/WellList.vue';
import WellForm from '@/component/form/WellForm.vue';
import WellGenericTable from '@/component/tables/WellGenericTable.vue';
import ImportButton from '@/component/buttons/ImportButton.vue';

export default {
  name: 'Wells',
  components: {
    ImportButton,
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
