<template>
  <div>
    <b-container>
      <h2 class="text-center my-3">Sandbox</h2>
      <b-card>
        <l-map ref="leafmap"
               :center="center"
               style="height: 600px">
          <l-tile-layer :url="openStreetMapUrl"></l-tile-layer>
          <l-polygon :color="polygon.color" :lat-lngs="polygon.latlngs"></l-polygon>
          <l-marker v-for="(marker,index) in markers" :key="index"
                    :lat-lng="[marker.lat, marker.lng]"
                    :offset="[10, 10]">
            <l-popup>
              <p>Скважина
                <router-link
                  to="#"
                  @click="click">
                  {{ marker.label }}
                </router-link>
              </p>
            </l-popup>
            <l-icon>
              <WellIcon :label="marker.label" :wellType="marker.type"/>
            </l-icon>
          </l-marker>
        </l-map>
      </b-card>
    </b-container>
  </div>
</template>

<script>
import {
  LIcon, LMap, LMarker, LPolygon, LPopup, LTileLayer,
} from 'vue2-leaflet';
import WellIcon from '../component/icons/WellIcon.vue';

export default {
  name: 'Sandbox',
  components: {
    WellIcon,
    LIcon,
    LMap,
    LPopup,
    LMarker,
    LTileLayer,
    LPolygon,
  },
  data() {
    return {
      openStreetMapUrl: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      satelliteUrl: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
      doubleGisUrl: 'http://tile2.maps.2gis.com/tiles?x={x}&y={y}&z={z}',
      center: [57.2, 65.6],
      markers: [
        {
          type: 'водозаборная', label: '99R', lat: 57.1, lng: 65.2,
        },
        {
          type: 'разведочная', label: '3028', lat: 57.3, lng: 65.4,
        },
        {
          type: 'поглощающая', label: '3029', lat: 57.14, lng: 65.6,
        },
      ],
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
  methods: {
    click() {
      console.log('Click');
      this.$toasted.show('Click');
    },
  },
};
</script>
