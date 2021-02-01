<template>
  <div>
    <b-card>
      <b-tabs content-class="mt-3">
        <b-tab active title="Общие данные">
          <FieldForm/>
        </b-tab>
        <b-tab v-for="(table, index) in tables" :key="index" :title="table.label">
          <GenericFieldTable :tableName="table.key"/>
        </b-tab>

      </b-tabs>
    </b-card>
  </div>
</template>

<script>
import FieldForm from '@/component/form/FieldForm.vue';
import GenericFieldTable from '@/component/tables/GenericFieldTable.vue';

export default {
  name: 'FieldData',
  components: { FieldForm, GenericFieldTable },
  data() {
    return {
      tables: [
        { label: 'Координаты', key: 'coordinates' },
        { label: 'Инклинометрия', key: 'inclinometry' },
        { label: 'МЭР', key: 'mer' },
        { label: 'Режимы', key: 'rates' },
        { label: 'Пласты', key: 'zones' },
      ],
    };
  },
};
</script>

<style scoped>

</style>
