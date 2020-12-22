<template>
  <ExploratoryWellIcon v-if="wellType==='разведочная'" :label="label"/>
  <GenericWellIcon v-else-if="wellType==='водозаборная'" :label="label" color="blue"/>
  <GenericWellIcon v-else-if="wellType==='поглощающая'" :label="label" color="green"/>
  <GenericWellIcon v-else :label="label"/>
</template>

<script>
import GenericWellIcon from './GenericWellIcon.vue';
import ExploratoryWellIcon from './ExploratoryWellIcon.vue';

export default {
  name: 'WellIcon',
  components: { ExploratoryWellIcon, GenericWellIcon },
  props: {
    label: String,
    wellType: {
      type: String,
      default: 'generic',
    },
  },
};
</script>

<style scoped>

</style>
