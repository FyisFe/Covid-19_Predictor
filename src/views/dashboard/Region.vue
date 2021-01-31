<template>
    <div class="region ml-1">
        <div class="region-header d-flex justify-content-between  align-items-center flex-wrap pb-3 mb-3">
            <div class="ml-2 d-flex align-items-center">
                <h4 class="mb-0 font-weight-bold">
                    Region Trends
                </h4>
                <div class="position-relative">
                    <button v-if="!isRunning" @click="send()" class="btn btn-calendar tx-12 btn-sm btn-rounded mx-3">
                        <span class="mx-2">
                            <font-awesome-icon class="mr-1" :icon="['fas', 'play']"></font-awesome-icon>
                            Run
                        </span>
                    </button>
                    <button v-else @click="pauseRunning()" class="btn btn-calendar tx-12 btn-sm btn-rounded mx-3">
                        <span class="mx-2">
                            <font-awesome-icon class="mr-1" :icon="['fas', 'pause']"></font-awesome-icon>
                            Pause
                        </span>
                    </button>
                    <button @click="reset()" class="btn btn-calendar tx-12 btn-sm btn-rounded mr-3">
                        <span class="mx-2">
                            <font-awesome-icon class="mr-1" :icon="['fas', 'sync-alt']"></font-awesome-icon>
                            Reset
                        </span>
                    </button>
                </div>
                <div class="region-breadcrumb text-muted d-none d-md-flex align-items-center">
                    Dashboard
                    <font-awesome-icon class="mx-1 right-icon" :icon="['fas', 'chevron-right']"></font-awesome-icon>
                    Region
                </div>
            </div>
            <div class="d-flex align-items-center">
                <button v-b-toggle.sidebar-controller :disabled='isRunning'
                    class="btn btn-editor btn-sm mr-3 d-md-block d-none"> <span class="mx-2">Editor</span></button>
                <button class="btn btn-data-export btn-sm d-md-block d-none"> <span class="mx-2">Data
                        Export</span></button>
            </div>
        </div>
        <div class="row">
            <div class="col-md-8 col-sm-12 grid-margin">
                <div class="card">
                    <div class="card-body">
                        <h6 class="card-title d-flex justify-content-between">
                            <div>Overall Trend</div>
                            <div>Day {{currentDay}}</div>
                        </h6>
                        <p class="mb-3 shade-color text-muted">
                            Get to know the overall trend during the period selected.
                        </p>
                       <lineChart ref="lineChart"></lineChart>
                    </div>
                </div>
            </div>
            <div class="col-md-4 col-sm-12 grid-margin stretch-card">
                <div class="card">
                    <div class="card-body">
                        <h6 class="card-title d-flex align-items-center justify-content-center">
                            <div>Day Controller</div>
                        </h6>
                        <pieChart ref="pieChart"></pieChart>
                        <div v-if="!isDestoried" class="fontLg controller d-flex flex-row justify-content-between">
                            <div @click="changeCurrentDay(currentDay - 1)">
                                <font-awesome-icon class="changeDay right-icon" :icon="['fas', 'chevron-circle-left']">
                                </font-awesome-icon>
                            </div>
                            <div @click="startChangeDay" v-if="!isChangingDay">
                                <button class="btn btn-data-export btn-sm d-md-block"> <span class="mx-2">Day
                                        {{currentDay}}</span></button>
                            </div>
                            <div v-else>
                                <b-form-input id="input-day" v-model="tempCurrentDay" :state="nameState"
                                    aria-describedby="input-day-feedback" placeholder="Enter Day"
                                    @blur="changeCurrentDay(tempCurrentDay)">
                                </b-form-input>
                                <b-form-invalid-feedback id="input-day-feedback">
                                    Enter reasonable day
                                </b-form-invalid-feedback>
                            </div>
                            <div @click="changeCurrentDay(currentDay + 1)">
                                <font-awesome-icon class="changeDay right-icon" :icon="['fas', 'chevron-circle-right']">
                                </font-awesome-icon>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-8 col-sm-12 grid-margin">
                <div class="card">
                    <div class="card-body">
                        <h6 class="card-title d-flex justify-content-between">
                            <div>Recover VS Dead</div>
                            <div>Day {{currentDay}}</div>
                        </h6>
                        <p class="mb-3 shade-color text-muted">
                            Get to know the situation of recovered and dead people  
                        </p>
                        <rvdChart ref="rvdChart">
                        </rvdChart>
                    </div>
                </div>
            </div>
            <div class="col-md-4 col-sm-12 grid-margin stretch-card">
                <div class="card">
                    <div class="card-body d-flex justify-content-between flex-column">
                        <h6 class="card-title d-flex align-items-center justify-content-center">
                            <div>Hospitalizations per Day</div>
                        </h6>
                        <p class="text-center mb-3 shade-color text-muted">
                            How many people are Hospitalized per day 
                        </p>
                        <gaugeChart ref="gaugeChart"></gaugeChart>
                    </div>
                </div>
            </div>
        </div>
        <b-sidebar id="sidebar-controller" title="Set parameter" backdrop shadow>
            <div class="px-3 py-2 small">
                <label for="input-s0">S0:</label>
                <b-form-input :disabled='!isDone' size="sm" id="input-s0" v-model="queryData.S0" placeholder="Enter S0"
                    trim>
                </b-form-input>
                <label class="mt-2" for="input-E0">E0:</label>
                <b-form-input :disabled='!isDone' size="sm" id="input-E0" v-model="queryData.E0" placeholder="Enter E0"
                    trim>
                </b-form-input>
                <label class="mt-2" for="input-I0">I0:</label>
                <b-form-input :disabled='!isDone' size="sm" id="input-I0" v-model="queryData.I0" placeholder="Enter I0"
                    trim>
                </b-form-input>
                <label class="mt-2" for="input-Sq0">Sq0:</label>
                <b-form-input :disabled='!isDone' size="sm" id="input-Sq0" v-model="queryData.Sq0"
                    placeholder="Enter Sq0" trim>
                </b-form-input>
                <label class="mt-2" for="input-Eq0">Eq0:</label>
                <b-form-input :disabled='!isDone' size="sm" id="input-Eq0" v-model="queryData.Eq0"
                    placeholder="Enter Eq0" trim>
                </b-form-input>
                <label class="mt-2" for="input-H0">H0:</label>
                <b-form-input :disabled='!isDone' size="sm" id="input-H0" v-model="queryData.H0" placeholder="Enter H0"
                    trim>
                </b-form-input>
                <label class="mt-2" for="input-R0">R0:</label>
                <b-form-input :disabled='!isDone' size="sm" id="input-R0" v-model="queryData.R0" placeholder="Enter R0"
                    trim>
                </b-form-input>
                <label class="mt-2" for="input-T">T:</label>
                <b-form-input size="sm" id="input-T" v-model="queryData.T" placeholder="Enter T" trim>
                </b-form-input>
                <label class="mt-2" for="input-l">l:</label>
                <b-form-input size="sm" id="input-l" v-model="queryData.l" placeholder="Enter l" trim>
                </b-form-input>
                <label class="mt-2" for="input-v">v:</label>
                <b-form-input size="sm" id="input-v" v-model="queryData.v" placeholder="Enter v" trim>
                </b-form-input>
                <label class="mt-2" for="input-e">e:</label>
                <b-form-input size="sm" id="input-e" v-model="queryData.e" placeholder="Enter e" trim>
                </b-form-input>
            </div>
        </b-sidebar>
    </div>
</template>

<script>
    import lineChart from '../../components/graph/lineChart.vue'
    import pieChart from '../../components/graph/pieChart.vue'
    import rvdChart from '../../components/graph/recoverDeadLineChart.vue'
    import gaugeChart from '../../components/graph/gaugeChart.vue'
    import axios from 'axios';
    export default {
        data() {
            return {
                currentDay: 0,
                totalAnimationDuration: 3,
                isRunning: false,
                isDestoried: false,
                isChangingDay: false,
                tempCurrentDay: '',
                isDone: false,
                isStartedClicked: 0,
                queryData: {
                    "S0": 7507000,
                    "E0": 443,
                    "I0": 259,
                    "Sq0": 1000,
                    "Eq0": 200,
                    "H0": 811,
                    "R0": 9302,
                    "D0": 178,
                    "T": 60,
                    "l": "1/14",
                    "v": 0.0013,
                    "e": 0.95
                },
                rawData: []
            }
        },
        computed: {
            animationInterval: function () {
                return (this.totalAnimationDuration / this.queryData.T) * 1000
            },
            nameState() {
                return (this.tempCurrentDay > 0 && this.tempCurrentDay <= this.queryData.T) ? true : false
            },
        },
        mounted() {
            this.send()
        },
        methods: {
            send() {
                this.isStartedClicked++
                if (this.currentDay == this.queryData.T) {
                    return
                }
                axios.post("http://127.0.0.1:3000/data", this.queryData, {
                        headers: {
                            'Authorization': 'Bearer' + 'Your Bearer Pssword',
                            "Content-Type": "application/json",
                        }
                    })
                    .then((response) => {
                        let temp = [];
                        for (let index = 0; index < 8; index++) {
                            temp.push([])
                        }
                        for (let index = 0; index < 8; index++) {
                            for (let i = 0; i < this.currentDay; i++) {
                                temp[index].push(this.rawData[index][i])
                            }
                        }
                        for (let index = 0; index < 8; index++) {
                            for (let i = this.currentDay; i < this.queryData.T; i++) {
                                temp[index].push(response.data[index][i])
                            }
                        }
                        this.rawData = temp;
                        this.$refs.lineChart.setData(this.rawData)
                        this.$refs.pieChart.setData(this.rawData)
                        this.$refs.rvdChart.setData(this.rawData)
                        this.$refs.gaugeChart.setData(this.rawData)
                        if (this.isStartedClicked == 1) {
                            this.$refs.lineChart.drawLine()
                            this.$refs.pieChart.drawPie()
                            this.$refs.rvdChart.drawLine()
                            this.$refs.gaugeChart.drawGraph()
                        }
                        this.isDone = false
                        this.startRunning()
                    })
                    .catch(function (error) {
                        console.log(error);
                    })
            },
            updateDay() {
                this.currentDay++
                this.$refs.lineChart.updateGraph(this.currentDay)
                this.$refs.pieChart.updateGraph(this.currentDay)
                this.$refs.rvdChart.updateGraph(this.currentDay)
                this.$refs.gaugeChart.updateGraph(this.currentDay)
            },
            startChangeDay() {
                if (this.isRunning) {
                    return
                }
                this.isChangingDay = true
            },
            changeCurrentDay(day) {
                if (day > this.queryData.T || day < 1 || this.isRunning) return
                this.currentDay = day
                this.$refs.lineChart.updateGraph(this.currentDay)
                this.$refs.pieChart.updateGraph(this.currentDay)
                this.$refs.rvdChart.updateGraph(this.currentDay)
                this.$refs.gaugeChart.updateGraph(this.currentDay)
                this.isChangingDay = false
                this.tempCurrentDay = ''
            },
            startRunning() {
                if (this.currentDay == this.queryData.T) {
                    this.isDone = true
                    return
                }
                if (this.isDestoried) {
                    this.isDestoried = !this.isDestoried
                }
                this.isRunning = true
                setTimeout(() => {
                    if (this.currentDay == this.queryData.T) {
                        this.isDone = true
                        this.isRunning = false
                        return
                    }
                    if (!this.isRunning) {
                        this.isRunning = false
                        return
                    }
                    this.updateDay()
                }, 0);
                var intervalID = null
                var runVisualize = () => {
                    if (this.currentDay == this.queryData.T) {
                        this.isDone = true
                        this.isRunning = false
                        clearInterval(intervalID)
                        return
                    }
                    if (!this.isRunning) {
                        this.isRunning = false
                        clearInterval(intervalID)
                        return
                    }
                    this.updateDay()
                }
                intervalID = setInterval(runVisualize, this.animationInterval);
            },
            reset() {
                this.currentDay = 0
                this.isDone = true
                this.isRunning = false
                this.isDestoried = true
                this.isStartedClicked = 0
                this.$refs.lineChart.reset()
                this.$refs.pieChart.reset()
                this.$refs.rvdChart.reset()
                this.$refs.gaugeChart.reset()
            },
            pauseRunning() {
                this.isRunning = false
            }
        },
        components: {
            lineChart,
            pieChart,
            rvdChart,
            gaugeChart
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

    .fontLg {
        font-size: 1.2rem;
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

    .grid-margin {
        margin-bottom: 1.25rem;
    }

    .card {
        border: 1px solid #353a53;
        position: relative;
        display: flex;
        flex-direction: column;
        background-color: #27293d;
        background-clip: border-box;
        border-radius: 0;
        height: 100%;
    }

    .card-title {
        color: #a7a7ba;
        margin-bottom: 0.625rem;
        text-transform: capitalize;
        font-size: .875rem;
        font-weight: 700;
    }

    .shade-color {
        color: #616172 !important;
        font-size: .875rem;
    }

    .changeDay {
        cursor: pointer;
        transition: .5s;
    }

    .changeDay:hover {
        font-size: .9rem;
        color: #fff;
    }
</style>