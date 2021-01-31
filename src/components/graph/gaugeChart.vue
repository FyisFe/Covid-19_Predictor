<template>
    <div class="w-100 d-flex justify-content-center"> 
        <div id="gague" style="width:333px; height: 300px"></div>
    </div>
</template>


<script>
    import * as echarts from 'echarts';

    export default {
        data() {
            return {
               chart: {},
               formatData: [], 
            }
        },
        mounted() {
        },
        methods: {
            drawGraph() {
                var chartDom = document.getElementById('gague');
                var myChart = echarts.init(chartDom);
                this.chart = myChart
                var option;

                option = {
                    series: [{
                        animation: false,
                        type: 'gauge',
                        progress: {
                            show: true,
                            width: 18
                        },
                        axisLine: {
                            lineStyle: {
                                width: 18
                            }
                        },
                        axisTick: {
                            show: false
                        },
                        splitLine: {
                            length: 1,
                            lineStyle: {
                                width: 1,
                                color: '#999'
                            }
                        },
                        axisLabel: {
                            distance: 25,
                            color: '#999',
                            fontSize: 11
                        },
                        anchor: {
                            show: true,
                            showAbove: true,
                            size: 10,
                            itemStyle: {
                                borderWidth: 10
                            }
                        },
                        title: {
                            show: false
                        },
                        detail: {
                            valueAnimation: true,
                            fontSize: 30,
                            color: '#7571f9',
                            opacity: .9,
                            offsetCenter: [0, '100%']
                        },
                        data: [{
                            value: 70
                        }]
                    }]
                };

                option && myChart.setOption(option);
            },
            updateGraph(day) {
                console.log(day);
                let option = this.chart.getOption()
                if (this.formatData[5][day] == undefined) {
                    return
                }
                option.series[0].data[0].value = this.formatData[5][day] - this.formatData[5][day-1]
                this.chart.setOption(option)
            },
            reset() {
                this.chart.dispose()
            },
            setData(data) {
                this.formatData = data
            }
        }
    }
</script>