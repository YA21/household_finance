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
          borderColor: 'red',
          data: [],
          fill: false,
          pointRadius: 0,
          lineTension: 0
        }]
      },
      options: {
        title: {
          display: true,
          text: ''
        },
        legend: {
          display: false
        }
      }
    }
  },
  mounted: function () {
    this.chartData.datasets[0].data = this.data
    this.chartData.datasets[0].borderColor = this.color
    this.chartData.datasets[0].label = this.kind
    this.options.title.text = this.kind
    this.renderChart(this.chartData, this.options)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
