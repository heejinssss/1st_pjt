import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import VueYoutube from 'vue-youtube'

Vue.config.productionTip = false 
Vue.use(VueYoutube)
Vue.use(BootstrapVue)

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')