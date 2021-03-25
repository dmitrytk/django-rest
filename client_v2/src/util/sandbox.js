const foo = () => {
  this.$store.commit('setField', { name: 'Foo' });
};

export default foo;
