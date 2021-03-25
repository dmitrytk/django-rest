<template>
  <v-container>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Калькулятор</div>
      </v-card-title>

      <v-layout align-center justify-center>
        <v-flex md4 sm8 xs12>
          <v-card-text>

            <v-text-field
              v-model="salinity"
              label="Минерализация, г/л"
              type="number"
              @keyup="calculate"
            ></v-text-field>

            <v-text-field
              v-model="temperature"
              label="Температура, С"
              type="number"
              @keyup="calculate"
            ></v-text-field>

            <v-text-field
              v-model="viscosity"
              disabled
              label="Вязкость, сПз"
            ></v-text-field>

            <v-text-field
              v-model="density"
              class="red--text"
              disabled
              label="Плотность, г/см3"
            ></v-text-field>

          </v-card-text>
        </v-flex>
      </v-layout>

    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'Calculator',
  data() {
    return {
      salinity: null,
      temperature: null,
      viscosity: null,
      density: null,
    };
  },
  methods: {
    calculate() {
      if (this.salinity > 0 && this.temperature > 0) {
        this.viscosity = this.calcViscosity(this.salinity, this.temperature);
        this.density = this.calcDensity(this.salinity, this.temperature);
      }
    },
    calcViscosity(salinity, temperature) {
      const a = temperature - 8.435;
      const distVisc = 100.0 / (2.1482 * (a + (8078.4 + a * a) ** 0.5) - 120.0);
      const am = 10 ** (-5) * (-2.24 * temperature + 14.0 * temperature ** 0.5 + 124.0);
      const viscosity = distVisc + am * salinity;
      return Math.round(viscosity * 1000) / 1000;
    },
    calcDensity(salinity, temperature) {
      const density = (1.0 - 5.9 * 10.0 ** (-6.0) * (temperature - 4.0) ** 1.95
        + 6.5 * salinity * 10.0 ** (-4)) / (1.0 - 4.2 * 10.0 ** (-5));
      return Math.round(density * 10000) / 10000;
    },

  },
};
</script>

<style scoped>

</style>
