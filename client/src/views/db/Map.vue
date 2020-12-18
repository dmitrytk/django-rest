<template>
  <div>
    <b-card>
      <l-map ref="leafmap"
             :center="center"
             :max-bounds="maxBounds"
             style="height: 500px">
        <l-tile-layer :url="url"></l-tile-layer>
        <l-polygon :color="polygon.color" :lat-lngs="polygon.latlngs"></l-polygon>
      </l-map>
    </b-card>
  </div>
</template>

<script>
import { latLngBounds } from 'leaflet';
import { LMap, LPolygon, LTileLayer } from 'vue2-leaflet';

export default {
  name: 'Map',
  components: {
    LMap,
    LTileLayer,
    LPolygon,
  },
  data() {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      center: [57.2, 65.6],
      polygon: {
        latlngs: [
          [57.1, 65.2],
          [57.3, 65.4],
          [57.14, 65.6],
          [57.1, 65.2],
        ],
        color: 'red',
      },
    };
  },
  mounted() {
    this.$refs.leafmap.mapObject.fitBounds(latLngBounds(this.polygon.latlngs));
  },
};
</script>
