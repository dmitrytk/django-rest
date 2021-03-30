<template>
  <div>
    <b-card v-if="polygon.latlngs.length>0">
      <div>
        <l-map ref="leafmap"
               :center="center"
               style="height: 600px">
          <l-tile-layer :url="satelliteUrl"></l-tile-layer>
          <l-polygon v-if="polygon.latlngs.length>0"
                     :color="polygon.color"
                     :lat-lngs="polygon.latlngs">
          </l-polygon>
          <l-layer-group v-if="markers.length>0">
            <l-marker
              v-for="(marker,index) in markers"
              :key="index"
              :lat-lng="[marker.lat, marker.lng]">
              <l-popup>
                <p>Скважина
                  <router-link
                    to="#">
                    {{ marker.label }}
                  </router-link>
                </p>
              </l-popup>
              <l-icon>
                <WellIcon :label="marker.label" :wellType="marker.type"/>
              </l-icon>
            </l-marker>
          </l-layer-group>

        </l-map>
        <b-button class="mt-3" @click="fitBounds">Подогнать</b-button>
      </div>
    </b-card>
    <h4 v-else class="text-center my-3">
      Нет координат месторождения
      <ImportButton/>
    </h4>
  </div>
</template>

<script>
import {
  LIcon, LLayerGroup, LMap, LMarker, LPolygon, LPopup, LTileLayer,
} from 'vue2-leaflet';
import WellIcon from '@/component/icons/WellIcon.vue';
import { mapGetters } from 'vuex';
import ImportButton from '@/component/buttons/ImportButton.vue';

export default {
  name: 'Map',
  components: {
    ImportButton,
    LMap,
    LTileLayer,
    LIcon,
    LLayerGroup,
    LPolygon,
    LPopup,
    LMarker,
    WellIcon,
  },
  data() {
    return {
      openStreetMapUrl: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      satelliteUrl: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
      doubleGisUrl: 'http://tile2.maps.2gis.com/tiles?x={x}&y={y}&z={z}',
      center: [0, 0],
      polygon: {
        latlngs: [],
        color: 'red',
      },
      markers: [],
    };
  },

  computed: {
    ...mapGetters('fields', [
      'field',
      'coordinates',
    ]),
    ...mapGetters('wells', [
      'wells',
    ]),
  },
  async mounted() {
    await this.getFieldCoordinates();
    await this.getWellsCoordinates();
    this.fitBounds();
  },
  methods: {
    getFieldCoordinates() {
      if (this.coordinates) {
        this.polygon.latlngs = this.coordinates
          .filter((c) => c.lat && c.lng)
          .map((c) => ({ lat: c.lat, lng: c.lng }));
      }
    },
    getWellsCoordinates() {
      if (this.wells) {
        console.log(this.wells);
        this.markers = this.wells
          .filter((w) => w.lat && w.lng)
          .map((w) => ({
            label: w.name, type: w.type, lat: w.lat, lng: w.lng,
          }));
      }
    },
    fitBounds() {
      if (this.$refs.leafmap && this.polygon.latlngs.length > 0) {
        this.$refs.leafmap.mapObject
          .fitBounds(this.polygon.latlngs.concat(this.markers), { padding: [5, 5] });
      }
    },
  },
};
</script>
