<template>
    <div class="w-100 d-flex justify-content-center">
        <div id="pie" style="width:333px; height: 300px"></div>
    </div>
</template>

<script>
    import * as echarts from 'echarts';

    export default {
        prop: {
            data: Array
        },
        data() {
            return {
                chart: {},
                chartData: [
                    [120, 132, 101, 134, 90, 230, 210, 120, 132, 101, 134, 90, 230, 210],
                    [220, 182, 191, 234, 290, 330, 310, 220, 182, 191, 234, 290, 330, 310],
                    [150, 232, 201, 154, 190, 330, 410, 150, 232, 201, 154, 190, 330, 410],
                    [320, 332, 301, 334, 390, 330, 320, 320, 332, 301, 334, 390, 330, 320],
                ],
                formatData: [],
                chartName: ['S', 'E', 'I', 'Sq', 'Eq', 'H', 'R', 'D']
            }
        },
        mounted() {
        },
        methods: {
            drawPie() {
                let chartDom = document.getElementById('pie')
                let myChart = echarts.init(chartDom)
                this.chart = myChart
                let option
                option = {
                    tooltip: {
                        trigger: 'item'
                    },
                    legend: {
                        top: '5%',
                        left: 'center',
                        textStyle: {
                            color: '#8c909a',
                            opacity: .9
                        }
                    },
                    series: [{
                        type: 'pie',
                        radius: ['30%', '60%'],
                        data: [],
                        labelLine: {
                            show: false
                        },
                        itemStyle: {
                            normal: {
                                label: {
                                    show: false
                                },
                                opacity: .9
                            },
                           
                        }
                    }],
                    animation: false
                };
             
                option && myChart.setOption(option);

            },
            updateGraph(day) {
                let option = this.chart.getOption()
                option.series[0].data = []
                for (let index = 0; index < 8; index++) {
                    let obj = {
                        value: this.formatData[index][day - 1],
                        name: this.chartName[index]
                    }
                    option.series[0].data.push(obj)
                }
                this.chart.setOption(option)
            },
            reset() {
                this.chart.dispose()
            },
            setData(data) {
                this.formatData = data
            }
        },
    }
</script>