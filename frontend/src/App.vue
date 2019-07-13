<template>
  <div id=app>
    <navigation-bar />
    <input-form
      @updateData="updateData"
    />
    <button v-on:click="apiPostTest">apiPostTest</button>
    <line-chart
      class=chart
      :data="[elecData, waterData, gasData]"
      :color="['yellow', 'blue', 'red']"
      :kind="['electricity', 'water', 'gas']"
      :key="lastUpdate"
    />
  </div>
</template>

<script>

import NavigationBar from './components/NavigationBar'
import InputForm from './components/InputForm'
import LineChart from './components/LineChart'
import axios from 'axios'

export default {
  name: 'app',
  components: { NavigationBar, InputForm, LineChart },
  props: {},
  data () {
    return {
      elecData: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      waterData: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      gasData: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      lastUpdate: Date.now(),
      formData: {
        month: 1
      }
    }
  },
  methods: {
    updateData (selectedKind, selectedMonth, inputData) {
      if (selectedKind == 'electricity') {
        this.elecData[selectedMonth - 1] = parseInt(inputData)
      } else if (selectedKind == 'water') {
        this.waterData[selectedMonth - 1] = parseInt(inputData)
      } else {
        this.gasData[selectedMonth - 1] = parseInt(inputData)
      }
      this.lastUpdate = Date.now()
    },
    apiPostTest () {
      const path = `http://0.0.0.0:5000/api/update_elec`
      axios.post(path, this.formData)
        .then(response => {
          console.log(response.data)
          console.log('ok')
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  mounted () {
    const path = `http://0.0.0.0:5000/api/getdata`
    axios.get(path)
      .then(response => {
        this.elecData = response.data.elec_data
        this.waterData = response.data.water_data
        this.gasData = response.data.gas_data
        this.lastUpdate = Date.now()
      })
      .catch(error => {
        console.log(error)
      })
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

.input-form {
  display: flex;
  width: 60%;
  margin: auto;
}
</style>
