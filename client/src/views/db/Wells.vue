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

          <!--    ФОРМА    -->
          <b-tabs content-class="mt-3">
            <b-tab active title="Общие данные">
              <WellForm/>
            </b-tab>

            <!--    ТАБЛИЦЫ    -->
            <GenericTableTab v-for="(table, index) in tables"
                             :key="index"
                             :parentId="well.id"
                             :tableName="table.key"
                             :title="table.label"
                             parent="wells"/>

            <!--    ДИАГРАММЫ    -->
            <ChartTab/>

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
import WellForm from '@/component/forms/WellForm.vue';
import GenericTableTab from '@/component/tables/GenericTableTab.vue';
import ImportButton from '@/component/buttons/ImportButton.vue';
import ChartTab from '@/component/ChartTab.vue';

export default {
  name: 'Wells',
  components: {
    ChartTab,
    ImportButton,
    GenericTableTab,
    WellList,
    WellForm,
  },
  data() {
    return {
      loading: false,
      tables: [
        { label: 'Инклинометрия', key: 'inclinometry' },
        { label: 'МЭР', key: 'mer' },
        { label: 'Режимы', key: 'rates' },
        { label: 'Пласты', key: 'zones' },
      ],
    };
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
      'mer',
      'rates',
    ]),
  },
  methods: {
    ...mapActions('fields', [
      'fetchFields',
    ]),

  },
};
</script>

<style scoped>

</style>
