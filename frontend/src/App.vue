<template>
  <div id=app>
    <navigation-bar />
    <input-form
      @updateElecData="updateElecData"
    />
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
      lastUpdate: Date.now()
    }
  },
  methods: {
    updateElecData (selectedMonth, inputData) {
      this.elecData[selectedMonth - 1] = parseInt(inputData)
      this.lastUpdate = Date.now()
    },
    apiTest () {
      const path = `http://localhost:5000/api/getelec`
      axios.get(path)
        .then(response => {
          this.elecData = response.data.elec_data
          this.lastUpdate = Date.now()
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

.input-form {
  display: flex;
  width: 60%;
  margin: auto;
}
</style>
