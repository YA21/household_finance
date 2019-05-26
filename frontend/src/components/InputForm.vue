<template>
  <div class="input-form">
    <select v-model="selectedMonth">
      <option v-for="month in months" :value=month.value :key=month.value>
        {{ month.text }}
      </option>
    </select>
    <b-form-input v-model="inputData" type="number"></b-form-input>
    <button class="btn btn-primary" v-on:click="updateElecData">Update</button>
  </div>
</template>

<script>
export default {
  props: {},
  data () {
    return {
      inputData: 0,
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
    updateElecData () {
      this.$emit('updateElecData', this.selectedMonth, this.inputData)
    }
  }
}
</script>

<style>
.input-form {
  display: flex;
  width: 60%;
  margin: auto;
}
</style>
