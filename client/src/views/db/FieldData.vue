<template>
  <div>
    <b-card>
      <b-tabs content-class="mt-3">
        <b-tab active title="Well data">
          <FieldForm/>
        </b-tab>
        <b-tab title="Inclinometry">
          <FieldInclinometryTable/>
        </b-tab>
      </b-tabs>
    </b-card>
  </div>
</template>

<script>
import FieldForm from '@/component/form/FieldForm.vue';
import FieldInclinometryTable from '@/component/tables/FieldInclinometryTable.vue';

export default {
  name: 'FieldData',
  components: { FieldInclinometryTable, FieldForm },
};
</script>

<style scoped>

</style>
