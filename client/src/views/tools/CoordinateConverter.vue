<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Конвертер координат</div>
      </v-card-title>
      <v-row>
        <!-- INPUT -->
        <v-col class="mb-3" lg="6">
          <h3 class="text-center text-secondary mb-3">Исходные</h3>
          <v-row class="mb-3">
            <v-col lg>
              <v-select v-model="selectedInType" :items="syst" label="Тип координаты"></v-select>
              <v-select v-model="selectedInSystem" :items="inSystem" label="Система координат">
              </v-select>

            </v-col>
            <v-col>
              <v-select
                v-if="selectedInType !== 'Геодезическая'"
                v-model="selectedInZone"
                :items="inZone"
                label="Зона">
              </v-select>
            </v-col>
          </v-row>

        </v-col>

        <!-- OUTPUT -->
        <v-col class="" lg="6">
          <h3 class="text-center text-secondary mb-3">Результат</h3>
          <v-row class="mb-3">
            <v-col lg>
              <v-select v-model="selectedOutType"
                        :items="syst"
                        label="Тип координаты">
              </v-select>
              <v-select v-model="selectedOutSystem"
                        :items="outSystem"
                        label="Система координат">
              </v-select>
            </v-col>
            <v-col>
              <v-select
                v-if="selectedOutType !== 'Геодезическая'"
                v-model="selectedOutZone"
                :items="outZone"
                label="Зона">
              </v-select>
              <v-radio-group id="degreeType" v-model="degreeType" row>
                <v-radio
                  value="ГГ MM СС.с"
                />
                ГГ MM СС.с
                <v-radio
                  class="ml-3"
                  value="ГГ.гггггг"
                />
                ГГ.гггггг
              </v-radio-group>
            </v-col>
          </v-row>
        </v-col>
      </v-row>

      <!-- TEXT AREAS -->
      <v-row>
        <v-col class="mb-3" lg="6">
          <v-textarea v-model="inData" class="form-control" rows="10"/>
        </v-col>
        <v-col class="mb-3" lg="6">
          <v-textarea v-model="outData" class="form-control" rows="10"/>
        </v-col>
      </v-row>

      <!-- BUTTONS -->
      <div class="text-left">
        <v-btn :disabled="!inData" class="mr-3 mt-3"
               variant="primary"
               @click="convert">
          <v-icon>mdi-play</v-icon>
          Конвертировать
        </v-btn>

        <CopyButton :target="outData" class="mt-3"/>
        <ClearButton :callback="clear" class="mt-3"/>
      </div>
    </v-card>

  </v-container>
</template>

<script>
import CopyButton from '@/components/buttons/CopyButton.vue';
import ClearButton from '@/components/buttons/ClearButton.vue';
import { coordinates } from '@/util/mock';
import systems from '@/util/coordinate/systems';
import convert from '@/util/coordinate/convert';

export default {
  name: 'CoordinateConverter',
  components: { ClearButton, CopyButton },
  title: 'Конвертер координат',
  data() {
    return {
      syst: Object.keys(systems),
      conv: convert,
      selectedInType: 'Геодезическая',
      selectedInSystem: 'СК42',
      selectedInZone: '',
      selectedOutType: 'Геодезическая',
      selectedOutSystem: 'СК42',
      selectedOutZone: '',
      inData: coordinates,
      outData: null,
      degreeType: 'ГГ MM СС.с',
    };
  },

  computed: {
    inSystem() {
      return Object.keys(systems[this.selectedInType]);
    },
    inZone() {
      return this.selectedInType !== 'Геодезическая'
        ? Object.keys(systems[this.selectedInType][this.selectedInSystem])
        : null;
    },
    outSystem() {
      return Object.keys(systems[this.selectedOutType]);
    },
    outZone() {
      return this.selectedOutType !== 'Геодезическая'
        ? Object.keys(systems[this.selectedOutType][this.selectedOutSystem])
        : null;
    },
  },

  methods: {
    convert() {
      try {
        this.outData = convert(
          this.selectedInType,
          this.selectedInSystem,
          this.selectedInZone,
          this.inData,
          this.selectedOutType,
          this.selectedOutSystem,
          this.selectedOutZone,
          this.degreeType,
          this.outData,
        );
      } catch (err) {
        console.log(err);
      }
    },
    clear() {
      this.inData = null;
      this.outData = null;
    },
  },
};
</script>

<style lang="scss">
#degreeType {
  padding: 6px;
}
</style>
