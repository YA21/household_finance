<script>
import { Line } from 'vue-chartjs'

export default {
  name: 'LineChart',
  extends: Line,
  props: [ 'data', 'color', 'kind' ],
  data () {
    return {
      chartData: {
        labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        datasets: [{
          label: '',
          borderColor: '',
          data: [],
          fill: false,
          pointRadius: 0,
          lineTension: 0
        }, {
          label: '',
          borderColor: '',
          data: [],
          fill: false,
          pointRadius: 0,
          lineTension: 0
        }, {
          label: '',
          borderColor: '',
          data: [],
          fill: false,
          pointRadius: 0,
          lineTension: 0
        }]
      },
      options: {
        title: {
          display: true,
          text: 'housefold finance'
        },
        legend: {
          display: true
        }
      }
    }
  },
  mounted: function () {
    for (let i in this.data) {
      this.chartData.datasets[i].data = this.data[i]
      this.chartData.datasets[i].borderColor = this.color[i]
      this.chartData.datasets[i].label = this.kind[i]
    }
    this.renderChart(this.chartData, this.options)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
