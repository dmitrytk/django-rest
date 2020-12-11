<template>
  <b-container>
    <h1 v-if="this.$store.state.field" class="text-center my-3">
      {{ this.$store.state.field.name }} месторождение
    </h1>
    <b-row v-if="this.$store.state.wells && this.$store.state.wells.length>0">
      <b-col lg="3">
        <b-card>
          <b-list-group>
            <b-list-group-item
              v-for="well in this.$store.state.wells" :key="well.id">
              {{ well.name }}
            </b-list-group-item>
          </b-list-group>
        </b-card>

      </b-col>
      <b-col lg="9">
        <b-card>
          <WellForm/>
        </b-card>
      </b-col>
    </b-row>

    <b-modal
      v-model="showFieldSelection"
      no-fade
      title="База данных"
      @ok="loadField"
    >
      <b-form-select
        v-model="selectedField"
        :options="fields">
        <template #first>
          <b-form-select-option :value="null" disabled>
            -- Выберите месторождение --
          </b-form-select-option>
        </template>
      </b-form-select>
    </b-modal>
    <b-button class="mt-3" @click="changeDB">Сменить базу</b-button>
  </b-container>
</template>

<script>
import FieldService from '@/service/FieldService';
import WellForm from '@/component/form/WellForm.vue';
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'DB',
  components: { WellForm },
  data() {
    return {
      loading: false,
      showFieldSelection: false,
      selectedField: null,
      fields: [],
      field: null,
    };
  },
  mounted() {
    if (!this.$store.state.field) {
      this.loadFields();
    }
  },
  computed: {
    ...mapGetters('fields', [
      'field',
      'fields',
      'isLoading',
    ]),
  },
  methods: {
    ...mapActions('fields', [
      'fetchFields',
    ]),
    loadFields() {
      FieldService.findAll()
        .then((res) => {
          this.fields = res.data.map((el) => ({ value: el.id, text: el.name }));
          this.showFieldSelection = true;
        });
    },
    async loadField() {
      if (!this.$store.state.field || this.$store.state.field.id !== this.selectedField) {
        await FieldService.findOne(this.selectedField)
          .then((res) => {
            this.field = res.data;
            this.$store.commit('setField', res.data);
          });
        FieldService.getWells(this.$store.state.field.id)
          .then((res) => {
            this.wells = res.data;
            this.$store.commit('setWells', res.data);
          });
      }
    },
    changeDB() {
      this.loadFields();
      this.showFieldSelection = true;
    },
    showWells() {
      console.log(this.$store.state.wells);
    },
  },
};
</script>

<style scoped>

</style>
