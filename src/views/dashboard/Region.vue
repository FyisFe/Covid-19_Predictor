<template>
    <div class="region ml-1">
        <div class="region-header d-flex justify-content-between  align-items-center flex-wrap pb-3 mb-3">
            <div class="ml-2 d-flex align-items-center">
                <h4 class="mb-0 font-weight-bold">
                    Region Trends
                </h4>
                <div class="position-relative">
                <button @click="isCalendarDisplayed = !isCalendarDisplayed" class="btn btn-calendar tx-12 btn-sm btn-rounded mx-3">
                    <span class="mx-2">
                        <font-awesome-icon class="mr-1" :icon="['fas', 'calendar-alt']"></font-awesome-icon>
                        Calendar
                    </span>
                </button>
                <b-calendar v-model="value" @context="onContext" locale="en-US" v-if="isCalendarDisplayed" class="region-calendar position-absolute"></b-calendar>
                </div>
                    <div class="region-breadcrumb text-muted d-none d-md-flex align-items-center">
                    Dashboard
                    <font-awesome-icon class="mx-1 right-icon" :icon="['fas', 'chevron-right']"></font-awesome-icon>
                    Region
                </div>
            </div>
            <div class="d-flex align-items-center">
                <button class="btn btn-editor btn-sm mr-3 d-md-block d-none"> <span class="mx-2">Editor</span></button>
                <button class="btn btn-data-export btn-sm d-md-block d-none"> <span class="mx-2">Data
                        Export</span></button>
            </div>
        </div>
        <div id="gauge" class="mt-5" style="width:500px; height: 500px"></div>
        <div id="line" class="mt-5" style="width:500px; height: 500px"></div>
        <div id="pie" class="mt-5" style="width:500px; height: 500px"></div>
    </div>
</template>

<script>
    import * as echarts from 'echarts';
    export default {
        data() {
            return {
                region_calendar: '',
                context: null,
                isCalendarDisplayed: false
            }
        },
        mounted() {
                this.drawGauge(),
                this.drawPie(),
                this.drawLine()
        },
        methods: {
            onContext(ctx) {
                this.context = ctx
            },
            drawGauge() {
                var chartDom = document.getElementById('gauge');
                var myChart = echarts.init(chartDom);
                var option;

                option = {
                    series: [{
                        type: 'gauge',
                        min: 0,
                        max: 100, //to be determined
                        axisLine: {
                            lineStyle: {
                                width: 30,
                                color: [
                                    [0.3, '#67e0e3'],
                                    [0.7, '#37a2da'],
                                    [1, '#fd666d']
                                ]
                            }
                        },
                        pointer: {
                            itemStyle: {
                                color: 'auto'
                            }
                        },
                        axisTick: {
                            distance: -30,
                            length: 8,
                            lineStyle: {
                                color: '#fff',
                                width: 2
                            }
                        },
                        splitLine: {
                            distance: -30,
                            length: 30,
                            lineStyle: {
                                color: '#fff',
                                width: 4
                            }
                        },
                        axisLabel: {
                            color: 'auto',
                            distance: 40,
                            fontSize: 20,
                            //use to change label
                            //   formatter: function(value) {
                            //         if (value === 0.5) {
                            //             return '2/4';
                            //         }
                            //         if (value === 1) {
                            //             return '4/4';
                            //         }
                            //         return value;
                            //     }
                        },
                        detail: {
                            valueAnimation: true,
                            formatter: function (value) {
                                return '{title|Adminssion Rate\n}{value|' + value + ' person/day}';
                            },
                            rich: {
                                title: {
                                    fontSize: 30,
                                    fontWeight: 'bolder',
                                    color: '#000',

                                },
                                value: {
                                    fontSize: 25,
                                    color: 'auto',

                                },

                            }

                        },
                        data: [{
                            value: 70
                        }]
                    }]
                };

                //change chart value
                setInterval(function () {
                    option.series[0].data[0].value = (Math.random() * 100).toFixed(0) - 0;
                    myChart.setOption(option, true);
                }, 2000);

                option && myChart.setOption(option);

            },
            drawLine() {
                var chartDom = document.getElementById('line');
                var myChart = echarts.init(chartDom, 'dark');
                var option;

                var name = ['S', 'E', 'I', 'R']; //here to be replaced by real name
                var data = [
                    [120, 132, 101, 134, 90, 230, 210],
                    [220, 182, 191, 234, 290, 330, 310],
                    [150, 232, 201, 154, 190, 330, 410],
                    [320, 332, 301, 334, 390, 330, 320]
                ];
                //here the data can be replaced by real data
                var dateNum = ['day1', 'day2', 'day3', 'day4', 'day5', 'day6',
                    'day7'
                ] //can be changed to number of days here
                option = {
                    animation: true,
                    animationDuration: 20000,

                    title: {
                        text: 'general analysis'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: name
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: true,
                        data: dateNum,
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [

                    ],
                };

                function genData() {
                    var series = option.series;
                    for (var i = 0; i < name.length; i++) {
                        series.push({
                            name: name[i],
                            type: 'line',
                            data: data[i]
                        });
                    }
                }

                genData();

                option && myChart.setOption(option);

            },
            drawPie() {
                var chartDom = document.getElementById('pie');
                var myChart = echarts.init(chartDom);
                var option;

                var data = [
                    [120, 132, 101, 134, 90, 230, 210],
                    [220, 182, 191, 234, 290, 330, 310],
                    [150, 232, 201, 154, 190, 330, 410],
                    [320, 332, 301, 334, 390, 330, 320]
                ];
                //here the data can be replaced by real data
                var count = 0;

                option = {
                    title: {
                        text: 'general analysis pie',
                        subtext: '',
                        left: 'center'
                    },
                    tooltip: {
                        trigger: 'item'
                    },
                    legend: {
                        orient: 'vertical',
                        left: 'left',
                    },
                    series: [{
                        name: 'data',
                        type: 'pie',
                        radius: '50%',
                        data: [{
                                value: 1048,
                                name: 'S'
                            },
                            {
                                value: 735,
                                name: 'E'
                            },
                            {
                                value: 580,
                                name: 'I'
                            },
                            {
                                value: 484,
                                name: 'R'
                            },
                        ],
                    }]
                };

                function run() {
                    var series = option.series[0].data;
                    if (count < data[0].length) {
                        for (var i = 0; i < series.length; i++) {
                            series[i].value = data[i][count];
                        }
                        count++;
                        option.title.subtext = 'day' + count;
                    }
                    myChart.setOption(option);
                }

                setInterval(function () {
                    run();
                }, 1000);

                option && myChart.setOption(option);

            }
        }
    }
</script>

<style lang="scss" scoped>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700&display=swap');

    .region {
        color: #a7a7ba;
        font-family: "Roboto", sans-serif;
    }

    .region-breadcrumb {
        font-size: .8em;
    }

    .region-header {
        border-bottom: 1px solid #353a53;
    }

    .right-icon {
        font-size: .6em;
    }

    .btn-calendar {
        color: #00BBE0;
        background-color: rgba(0, 187, 224, 0.2);
        border-color: rgba(0, 187, 224, 0);
        border-radius: 20px;
        font-size: .8em;
        position: relative;
    }

    .btn-calendar:hover {
        background-color: #00BBE0;
        color: #ffffff;
    }

    .btn-editor {
        background-color: #7571f9;
        color: #fff;
        border-radius: 0;
    }

    .btn-editor:hover {
        background-color: #4b45f8;
    }

    .btn-data-export {
        border-color: #7571f9;
        color: #7571f9;
        border-radius: 0;
    }

    .btn-data-export:hover {
        background: #7571f9;
        color: #fff;
    }

    .region-calendar {
        top: 35px;
        left: 0;
        z-index: 1000;
    }

    h4 {
        font-size: 1.3em;
    }
</style>