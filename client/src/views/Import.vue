<template>
  <div class="container">
    <h2 class="text-center my-3">Импорт данных</h2>
    <b-card v-if="loaded">
      <b-form inline>
        <label class="mr-sm-2">Тип данных</label>
        <b-form-select
          v-model="selectedDataType"
          :options="dataTypes"
          class="mb-2 mr-sm-2 mb-sm-0"
        ></b-form-select>
      </b-form>
      <b-form-textarea
        v-model="content"
        class="mt-3"
        max-rows="10"
        placeholder="Введите данные"
        rows="10"
        @keyup="parse"
      ></b-form-textarea>
      <b-button class="mt-3 mr-3" variant="primary" @click="load">Загрузить</b-button>
      <b-button class="mt-3 mr-3" variant="danger" @click="clear">Очистить</b-button>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'Import',
  data() {
    return {
      loaded: true,
      content: '',
      dataTypes: [
        { value: 'wells', text: 'Скважины' },
        { value: 'rates', text: 'Режимы' },
        { value: 'mer', text: 'МЭР' },
        { value: 'zones', text: 'Пласты' },
        { value: 'inclinometry', text: 'Инклинометрия' },
      ],
      selectedDataType: 'wells',
    };
  },
  mounted() {
  },
  methods: {
    parse() {
      console.log('parse');
    },
    load() {
      console.log('load');
    },
    clear() {
      this.content = '';
    },
  },
};
</script>

<style scoped>

</style>
