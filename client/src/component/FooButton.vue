<template>
  <b-button @click="foo">Change DB</b-button>
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
