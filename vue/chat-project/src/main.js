import Vue from 'vue'
import App from './App.vue'
//import VueMomentJS from 'vue-momentjs'

Vue.config.productionTip = false
//Vue.use(VueMomentJS, moment)
Vue.use(require('vue-moment'));

new Vue({
  render: h => h(App),
}).$mount('#app')
