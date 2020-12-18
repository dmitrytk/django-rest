<template>
  <div>
    <b-card>
      <l-map ref="leafmap"
             :center="center"
             :max-bounds="maxBounds"
             style="height: 500px">
        <l-tile-layer :url="doubleGisUrl"></l-tile-layer>
        <l-polygon :color="polygon.color" :lat-lngs="polygon.latlngs"></l-polygon>
      </l-map>
    </b-card>
  </div>
</template>

<script>
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
      openStreetMapUrl: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      satelliteUrl: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
      doubleGisUrl: 'http://tile2.maps.2gis.com/tiles?x={x}&y={y}&z={z}',
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
    this.$refs.leafmap.mapObject.fitBounds(this.polygon.latlngs);
  },
};
</script>
