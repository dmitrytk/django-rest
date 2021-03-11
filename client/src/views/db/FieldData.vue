<template>
  <div>
    <b-card>
      <b-tabs content-class="mt-3">

        <!--    ФОРМА    -->
        <b-tab active title="Общие данные">
          <FieldForm/>
        </b-tab>

        <!--    ТАБЛИЦЫ    -->
        <GenericTableTab v-for="(table, index) in tables"
                         :key="index"
                         :parentId="field.id"
                         :tableName="table.key"
                         :title="table.label"
                         parent="fields"/>

      </b-tabs>
    </b-card>
  </div>
</template>

<script>
import FieldForm from '@/component/forms/FieldForm.vue';
import GenericTableTab from '@/component/tables/GenericTableTab.vue';
import { mapGetters } from 'vuex';

export default {
  name: 'FieldData',
  components: { FieldForm, GenericTableTab },
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
  computed: {
    ...mapGetters('fields', ['field']),
  },
};
</script>

<style scoped>

</style>
