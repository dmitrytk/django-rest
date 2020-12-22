<template>
  <svg :height="radius*3" :width="radius*10">
    <circle
      :cx="radius+2"
      :cy="radius+2"
      :r="radius"
      fill-opacity="0"
      stroke="black"
      stroke-width="2"
    />
    <circle
      :cx="radius+2"
      :cy="radius+2"
      :r="radius*0.6"
      fill="black"
      stroke="black"
      stroke-width="2"
    />
    <text :x="radius*3" :y="radius*2" fill="black" font-size="14">{{ label }}</text>
  </svg>
</template>

<script>
export default {
  name: 'ExploratoryWellIcon',
  props: {
    label: {
      type: String,
      default: 'well',
    },
    color: {
      type: String,
      default: 'black',
    },
    radius: {
      type: Number,
      default: 10,
    },
  },
};
</script>
