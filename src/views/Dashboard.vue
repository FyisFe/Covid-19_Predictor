<template>
    <div class="dashboard">
        <b-navbar sticky toggleable="lg" type="dark" class="dashboard-navbar">
            <b-navbar-brand @click="toggleSidebar()" class="brand ml-3">
                <font-awesome-icon class="sidebar-toggler" :icon="['fas', 'bars']"></font-awesome-icon>
                Prophet
            </b-navbar-brand>
            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
                <router-link to="/">
                    <font-awesome-icon class="home-icon" :icon="['fas', 'home']"></font-awesome-icon>
                </router-link>
            </b-navbar-nav>
        </b-navbar>
        <div id="main-body" class="d-flex">
            <div id="sidebar-wrapper">
                <ul class="sidebar-list">
                    <li class="sidebar-list-item">
                        <a v-b-toggle.submenu-item :class="{active: dashboardActive}"
                            class="sidebar-list-item-link sidebar-list-submenu">
                            <font-awesome-icon class="sidebar-list-icon" :icon="['fas', 'tachometer-alt']">
                            </font-awesome-icon>
                            <span class="sidebar-list-title">Dashboard</span>
                            <font-awesome-icon class="sidebar-list-arrow" :icon="['fas', 'sort-down']">
                            </font-awesome-icon>
                        </a>
                    </li>
                    <b-collapse :visible='dashboardActive' id="submenu-item">
                        <ul class="sidebar-sublist">
                            <li class="sidebar-sublist-item">
                                <a href="region" class="sidebar-sublist-link" :class="{active: regionActive}">
                                    <font-awesome-icon :icon="['fas', 'chart-line']" class="mr-2"></font-awesome-icon>
                                    Regions
                                </a>
                            </li>
                            <li class="sidebar-sublist-item">
                                <a href="building" class="sidebar-sublist-link" :class="{active: buildingActive}">
                                    <font-awesome-icon :icon="['fas', 'building']" class="mr-2"></font-awesome-icon>
                                    Buildings
                                </a>
                            </li>
                        </ul>
                    </b-collapse>
                    <li class="sidebar-list-item">
                        <a href="" :class="{active: userGuideActive}" class="sidebar-list-item-link">
                            <font-awesome-icon class="sidebar-list-icon" :icon="['fas', 'book']">
                            </font-awesome-icon>
                            <span class="sidebar-list-title">User Guide</span>
                        </a>
                    </li>
                    <li class="sidebar-list-item">
                        <a href="" :class="{active: aboutUsActive}" class="sidebar-list-item-link">
                            <font-awesome-icon class="sidebar-list-icon" :icon="['fas', 'user']">
                            </font-awesome-icon>
                            <span class="sidebar-list-title">About Us</span>
                        </a>
                    </li>
                    <li class="sidebar-list-item">
                        <a href="" :class="{active: docActive}" class="sidebar-list-item-link">
                            <font-awesome-icon class="sidebar-list-icon" :icon="['fas', 'file-alt']">
                            </font-awesome-icon>
                            <span class="sidebar-list-title">Doc</span>
                        </a>
                    </li>
                </ul>
            </div>
            <!-- Page Content -->
            <div id="page-content-wrapper">
                <router-view></router-view>
            </div>
        </div>
    </div>
</template>
<script>
    import $ from 'jquery'
    export default {
        data() {
            return {
                userGuideActive: false,
                aboutUsActive: false,
                docActive: false,
                regionActive: false,
                buildingActive: false
            }
        },
        created() {
            this.setActiveSidebar();
        },
        computed: {
            dashboardActive: function () {
                return this.regionActive || this.buildingActive;
            }
        },
        methods: {
            toggleSidebar() {
                $("#main-body").toggleClass("toggled");
            },
            setActiveSidebar() {
                let routePath = this.$route.path;
                let page = routePath.split('/')[2];
                switch (page) {
                    case 'region':
                        this.regionActive = true;
                        break;
                    case 'building':
                        this.buildingActive = true;
                        break;
                    default:
                        break;
                }
            }
        },
    }
</script>
<style lang="scss" scoped>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700&display=swap');

    .dashboard {
        font-size: 1vw;
        width: 100vw;
    }

    .dashboard-navbar {
        background: #27293d;
        border-bottom: 1px solid #353a53;
        box-shadow: 1px 5px 10px #222334;
    }

    .dashboard-navbar .brand {
        background-color: #27293d;
        font-weight: 700;
        font-size: 1.2em;
        font-family: "Roboto", sans-serif;
        opacity: .8;
    }

    .dashboard-navbar .brand .sidebar-toggler {
        font-size: 0.9em;
    }

    .home-icon {
        color: #ffffff;
        opacity: .8;
        font-size: 1.2em;
        margin-right: 2rem;
    }
    .home-icon:hover {
        opacity: 1;
    }

    #main-body {
        background: #1e1e2f;
    }
    #main-body .sidebar-list {
        display: flex;
        padding-left: 0;
        list-style: none;
        overflow: hidden;
        flex-wrap: nowrap;
        flex-direction: column;
    }

    #sidebar-wrapper {
        width: 18%;
        font-family: "Roboto", sans-serif;
        font-weight: 400;
        padding: 0.6rem 1.25rem;
        background-color: #27293d;
        min-height: 100vh;
        margin-left: -20rem;
        border-right: 1px solid #353a53;
        -webkit-transition: margin .25s ease-out;
        -moz-transition: margin .25s ease-out;
        -o-transition: margin .25s ease-out;
        transition: margin .25s ease-out;
    }

    .sidebar-list-item {
        position: relative;
    }

    .sidebar-list-item:before {
        content: '';
        position: absolute;
        top: 0;
        left: 20px;
        right: 0;
        border-top: 1px dashed #353a53;
    }

    .sidebar-list-item-link {
        margin: 0;
        display: flex;
        align-items: center;
        white-space: nowrap;
        height: 2.5rem;
        padding: 0;
        color: #8c909a;
        font-size: 1em;
        text-decoration: none;
        position: relative;
    }

    .sidebar-list-item-link:hover {
        color: #7571f9;
    }

    .sidebar-list-item .active {
        color: #7571f9;
    }

    .sidebar-list-submenu::after {
        content: '';
        position: absolute;
        top: 0;
        left: 20px;
        right: 0;
        border-top: 1px dashed #353a53;
    }

    .sidebar-list-icon {
        margin-right: .8rem;
        margin-bottom: 2px;
    }

    .sidebar-list-arrow {
        display: inline-block;
        margin-left: auto;
        margin-right: 0;
        line-height: 10;
        margin-bottom: .3rem;
        transition: .3s;
    }

    .sidebar-list-title {
        display: inline-block;
        vertical-align: middle;
        line-height: 1;
        font-weight: 500;
    }

    .sidebar-sublist {
        margin-bottom: 0;
        margin-top: 0;
        list-style: none;
        padding: 0.25rem 0 0.5rem 1.9rem;
        overflow: hidden;
        flex-wrap: nowrap;
        display: flex;
        flex-direction: column;
    }

    .sidebar-sublist-item {
        position: relative;
        padding: 0;
        color: #8c909a;
        font-weight: 400;
        font-size: .8em;
        line-height: 1.9;
        display: flex;
        align-items: center;
    }

    .sidebar-sublist-item .active {
        color: #7571f9;
    }

    .sidebar-sublist-item:before {
        content: '';
        width: .12rem;
        height: 2.3rem;
        position: absolute;
        left: -1.4rem;
        background: #353a53;
    }

    .sidebar-sublist-link {
        padding: 0;
        height: 2rem;
        position: relative;
        font-size: 1.1em;
        color: #8c909a;
        text-decoration: none;
        line-height: 1;
        border-top: 0;
        display: flex;
        align-items: center;
        white-space: nowrap;
    }

    .sidebar-sublist-link:hover {
        color: #7571f9
    }

    .not-collapsed .sidebar-list-arrow {
        margin-top: .7em;
        transition: .3s;
        transform: rotate(180deg);
    }

    #page-content-wrapper {
        min-width: 100vw;
        padding: 1.25rem;
        width: 100%;
    }

    #main-body.toggled #sidebar-wrapper {
        margin-left: 0;
    }

    @media (min-width: 768px) {
        #sidebar-wrapper {
            margin-left: 0;
        }

        #page-content-wrapper {
            min-width: 0;
            width: 100%;
        }

        #main-body.toggled #sidebar-wrapper {
            margin-left: -20rem;
        }
    }
</style>