<template>
  <b-container>
    <h2 class="text-center my-3">Водный калькулятор</h2>

    <b-card>
      <!--      Salinity      -->
      <b-form-group
        label-for="input-default">
        <label for="salinity">Минерализация, г/л</label>
        <b-form-input
          id="salinity"
          v-model="salinity"
          type="number"
          @keyup="calculate">
        </b-form-input>
      </b-form-group>

      <!--      Temperature      -->
      <b-form-group
        label-for="input-default">
        <label for="temperature">Температура, &deg;C</label>
        <b-form-input
          id="temperature"
          v-model="temperature"
          type="number"
          @keyup="calculate">
        </b-form-input>
      </b-form-group>

      <!--      Viscosity      -->
      <b-form-group
        label-for="input-default">
        <label for="viscosity">Вязкость, сПз</label>
        <b-form-input id="viscosity" v-model="viscosity" type="number">
        </b-form-input>
      </b-form-group>

      <!--      Density      -->
      <b-form-group
        label-for="input-default">
        <label for="density">Плотность, г/см<sup>3</sup></label>
        <b-form-input id="density" v-model="density" type="number">
        </b-form-input>
      </b-form-group>
    </b-card>
  </b-container>
</template>

<script>
export default {
  name: 'WaterCalculator',
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
      console.log('calculate');
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
