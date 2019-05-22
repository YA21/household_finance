<template>
  <div id=app>
    <select v-model="selectedMonth">
      <option v-for="month in months" :value=month.value :key=month.value>
        {{ month.text }}
      </option>
    </select>
    <input v-model="inputData" type="number">
    <button v-on:click="updateElecData">Update</button>
    <button v-on:click="apiTest">apiTest</button>
    <line-chart
      class=chart
      :data="elecData"
      :color="'red'"
      :kind="'electricity'"
      :key="lastUpdate"
    />
  </div>
</template>

<script>

import LineChart from './components/LineChart'
import axios from 'axios'

export default {
  name: 'app',
  components: { LineChart },
  props: {},
  data () {
    return {
      elecData: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      inputData: 0,
      lastUpdate: Date.now(),
      selectedMonth: 0,
      months: [
        {text: 'Janualy', value: 1},
        {text: 'Februaly', value: 2},
        {text: 'March', value: 3},
        {text: 'April', value: 4},
        {text: 'May', value: 5},
        {text: 'June', value: 6},
        {text: 'July', value: 7},
        {text: 'August', value: 8},
        {text: 'September', value: 9},
        {text: 'October', value: 10},
        {text: 'November', value: 11},
        {text: 'December', value: 12}
      ]
    }
  },
  methods: {
    updateElecData: function () {
      this.elecData[this.selectedMonth - 1] = parseInt(this.inputData)
      this.lastUpdate = Date.now()
    },
    apiTest: function () {
      const path = 'http://localhost:5000/api/getelec'
      axios.get(path)
        .then(response => {
          this.elecData = response.data.elec_data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style>
.chart {
  width: 500px;
  height: 500px;
  margin: auto;
}

#app {
  text-align: center;
}
</style>
