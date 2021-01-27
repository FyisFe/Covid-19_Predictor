<template>
    <div class="container fixed-top home-navbar">
        <b-navbar toggleable="lg" type="dark">
            <b-navbar-brand class="nav-brand-text" href="#">
                <span class="text-uppercase text-heavier">
                    <font-awesome-icon :icon="['fas', 'chart-bar']"></font-awesome-icon>
                    Prophet •
                </span>
                <span> <i>Covid-19 Trend Predictor</i> </span>
            </b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto text-smaller pr-2">
                    <b-nav-item-dropdown text="Getting Started">
                        <b-dropdown-item href="/dashboard/building">
                            <font-awesome-icon :icon="['fas', 'building']" class="mr-2"></font-awesome-icon>Prediction
                            for Buildings
                        </b-dropdown-item>
                        <b-dropdown-item href="/dashboard/region">
                            <font-awesome-icon :icon="['fas', 'chart-line']" class="mr-2"></font-awesome-icon>Prediction
                            for Regions
                        </b-dropdown-item>
                    </b-nav-item-dropdown>
                    <b-nav-item href="#">
                        <font-awesome-icon :icon="['fas', 'book']" class="mr-2"></font-awesome-icon>User Guide
                    </b-nav-item>
                    <b-nav-item href="#">
                        <font-awesome-icon :icon="['fas', 'user']" class="mr-2"></font-awesome-icon>About Us
                    </b-nav-item>
                    <b-nav-item href="#">
                        <font-awesome-icon :icon="['fas', 'file-alt']" class="mr-2"></font-awesome-icon>Docs
                    </b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<style lang="scss">
    .home-navbar {
        background: 0px 0px !important;
        top: 1rem;
        font-weight: 200;
    }

    .home-navbar .nav-brand-text {
        font-size: 1.25vw;
    }

    .home-navbar .text-heavier {
        font-weight: 500;
    }

    .home-navbar .text-smaller {
        font-size: 0.875rem;
    }

    .home-navbar .dropdown-item {
        font-size: 0.75vw;
        color: #9a9a9a;
        padding-top: .6rem;
        padding-bottom: .6rem;
        margin-top: 5px;
    }

    .home-navbar .navbar-dark .navbar-nav .nav-link {
        color: #ffffffCC !important;
        padding-right: 2rem;
        font-size: 1vw;
    }

    .home-navbar .dropdown-menu:before {
        display: inline-block;
        position: absolute;
        width: 0;
        height: 0;
        vertical-align: middle;
        content: "";
        top: -5px;
        left: 10px;
        right: auto;
        color: #fff;
        border-bottom: .4em solid;
        border-right: .4em solid transparent;
        border-left: .4em solid transparent;
    }
</style>