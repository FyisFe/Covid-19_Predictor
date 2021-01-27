<template>
  <div class="home">
    <homeNavbar></homeNavbar>
    <div class="page-header">
      <img src="../assets/images/blob.png" class="path">
      <img src="../assets/images/path2.png" class="path2">
      <img src="../assets/images/triunghiuri.png" class="shapes triangle">
      <img src="../assets/images/waves.png" class="shapes waves">
      <img src="../assets/images/patrat.png" class="shapes square">
      <img src="../assets/images/cercuri.png" class="shapes circle">
      <div class="container-fluid">
        <div class="brand d-flex flex-column text-center align-items-center">
          <h1 class="h1-brand d-block">
            <span class="text-uppercase brand-name">
              <font-awesome-icon :icon="['fas', 'chart-bar']"></font-awesome-icon> Prophet •
            </span>
            <small class="brand-description">Covid-19 Trend Predictor</small>
          </h1>
          <h3 class="h3-brand mt-5">Start predicting the trend of Covid-19 in your company or regions through <span
              class="brand-description">PROPHET</span> right away </h3>
            <router-link to="/dashBoard/region" class="start-btn">Get Started</router-link>
          <a class="mt-4 guide-link" href="#">Read User Guide</a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  // @ is an alias to /src
  import homeNavbar from '../components/HomeNavbar'
  export default {
    components: {
      homeNavbar
    }
  };
</script>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,200;0,300;0,400;0,600;1,200;1,300&display=swap');

  .home {
    width: 100vw;
    height: 100vh;
    font-family: 'Poppins', sans-serif;
    font-size: .875vw;
    background-color: #171941;
  }

  .home .page-header {
    min-height: 100vh;
    position: relative;
    overflow: hidden;
    color: #fff;
    display: flex;
  }

  .home .page-header .container-fluid {
    position: absolute;
    margin-top: 11rem;
    display: flex;
    justify-content: center;
  }

  .home .page-header .container-fluid .brand {
    width: 45%;
  }

  .home .page-header .container-fluid .brand .h1-brand {
    font-size: 4em;
    font-weight: 400;
    opacity: 0.8;
  }

  .home .page-header .container-fluid .brand .brand-description {
    color: #ff8d72;
    font-weight: 600;
  }

  .home .page-header .brand .h3-brand {
    font-weight: 300;
    opacity: 0.8;
    line-height: 3rem;
    font-size: 1.8em;
  }

  .home .page-header .start-btn {
    width: 25%;
    font-size: 1.2em;
    position: relative;
    padding: 1.4em;
    color: #ff8d72;
    text-decoration: none;
    transition: 0.5s;
    margin-top: 2rem;
  }

  .home .page-header .start-btn::before{
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: .5rem;
    height: .5rem;
    border-top: 2px solid #ff8d72;
    border-left: 2px solid #ff8d72;
    transition: 0.5s;
  }

  .home .page-header .start-btn::after{
    content: '';
    position: absolute;
    bottom: 0;
    right: 0;
    width: .5rem;
    height: .5rem;
    border-bottom: 2px solid #ff8d72;
    border-right: 2px solid #ff8d72;
    transition: 0.5s;
  }
  .home .page-header .start-btn:hover::after {
    width: 100%;
    height: 100%;
    border-radius: .5rem;
  } 
   .home .page-header .start-btn:hover::before {
    width: 100%;
    height: 100%;
    border-radius: .5rem;
  } 
  .home .page-header .guide-link {
    text-decoration: underline;
    color: #fff;
    opacity: 0.9;
    font-size: 1em;
    transition: 0.6s;
  }

  .home .page-header .guide-link:hover {
    opacity: 1;
    font-size: 1.3em;
  }

  .home .path {
    max-width: 65%;
    right: 0;
    top: 30px;
    position: absolute;
    opacity: 0.02;
  }

  .home .path2 {
    position: absolute;
    opacity: 0.02;
    max-width: 41%;
    right: -60px;
    top: -50px;
    z-index: 2;
  }

  .home .shapes {
    position: absolute;
    opacity: 0.02;
    z-index: 2;
  }

  .home .triangle {
    top: 35%;
    left: 5%;
    max-height: 200px;
  }

  .home .square {
    top: 50%;
    right: 18%;
    max-height: 200px;
  }

  .home .waves {
    top: 45%;
    right: 30%;
    max-height: 90px;
  }

  .home .circle {
    top: 20%;
    right: 36%;
    max-height: 75px;
  }
</style>