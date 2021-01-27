import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/fontawesome'
import './plugins/bootstrap-vue'
import App from './app.vue'
import router from './router'

import jQuery from 'jquery'
global.$ = jQuery
Vue.config.productionTip = false
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
