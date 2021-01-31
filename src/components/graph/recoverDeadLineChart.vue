<template>
    <div class="w-100 d-flex justify-content-center">
        <div id="rvdLine" style="width: 740px; height: 300px"></div>
    </div>
</template>

<script>
    import * as echarts from 'echarts';
    export default {
        prop: {
            rawData: Array
        },
        data() {
            return {
                chart: {},
                formatData: []
            }
        },
        mounted() {
        },
        methods: {
            drawLine() {
                let chartDom = document.getElementById('rvdLine');
                let myChart = echarts.init(chartDom);
                this.chart = myChart
                let option;
                let name = ['R', 'D']; //here to be replaced by real name
                //here the data can be replaced by real data
                let dateNum = [
                ];
                for (let i = 1; i <= this.formatData[0].length; i++) {
                    let temp = 'Day ' + i
                    dateNum.push(temp) 
                }
                option = {
                    backgroundColor: '#27293d',
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: name,
                        textStyle: {
                            color: '#8c909a',
                        }
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: {
                        type: 'category',
                        data: dateNum,
                        boundaryGap: false,
                        axisLabel: {
                            textStyle: {
                                color: '#8c909a',
                                fontFamily: "Roboto"
                            },
                        },
                        axisLine: {
                            show: false
                        },
                        axisTick: {
                            show: false
                        },
                    },
                    yAxis: {
                        type: 'value',
                        axisLine: {
                            show: false
                        },
                        axisLabel: {
                            textStyle: {
                                color: '#8c909a',
                                fontFamily: '"Roboto", "sans-serif"'
                            }
                        },
                        splitLine: {
                            show: true,
                            lineStyle: {
                                color: ['#616172'],
                                opacity: 0.3
                            }
                        },
                    },
                    series: [],
                    animationDuration: 3/14 * 1000,
                    animationDurationUpdate: 3/14 * 1000,
                };

                function genData() {
                    let series = option.series;
                    for (let i = 0; i < name.length; i++) {
                        series.push({
                            name: name[i],
                            type: 'line',
                            data: [],
                            symbol: 'none',
                            lineStyle: {
                                opacity: 0.7
                            }
                        });
                    }
                }

                genData();

                option && myChart.setOption(option);

            },
            updateGraph(day) {
                let option = this.chart.getOption()
                for (let index = 6; index < 8; index++) {
                    option.series[index - 6].data = []
                    for (let i = 0; i < day; i++) {
                         option.series[index - 6].
                         data.push(this.formatData[index][i])
                    }   
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

<style lang="scss" scoped>

</style>