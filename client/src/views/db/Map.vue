<template>
  <div>
    <b-card>
      <GmapMap
        ref="mmm"
        :center="center"
        :zoom="12"
        map-type-id="terrain"
        style="width: 100%; height: 50vh"
      >
        <GmapMarker v-for="(marker, index) in markers"
                    :key="index"
                    :clickable="true"
                    :draggable="true"
                    :position="marker.position" @click="center=marker.position">
        </GmapMarker>
      </GmapMap>
    </b-card>
  </div>
</template>

<script>
import { gmapApi } from 'gmap-vue';

export default {
  name: 'Map',
  data() {
    return {
      center: {
        lat: 50,
        lng: 50,
      },
      markers: [{
        position: {
          lat: 10.0,
          lng: 10.0,
        },
      }, {
        position: {
          lat: 11.0,
          lng: 11.0,
        },
      }],
    };
  },
  computed: {
    google: gmapApi,
  },
  mounted() {
    this.fitBounds();
  },
  methods: {
    fitBounds() {
      this.$refs.mmm.$mapPromise.then((map) => {
        const bounds = new this.google.maps.LatLngBounds();
        this.markers.forEach((m) => {
          bounds.extend(m.position);
        });
        map.fitBounds(bounds);
      });
    },
  },
};
</script>
