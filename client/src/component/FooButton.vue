<template>
  <b-button @click="foo">Сменить базу</b-button>
</template>

<script>
export default {
  name: 'FooButton',
  methods: {
    foo() {
      this.$store.commit('setField', { name: 'Foo' });
    },
  },
};
</script>
