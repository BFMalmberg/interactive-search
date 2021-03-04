import Vue from 'vue';
import Vuex from 'vuex';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import VueResource from 'vue-resource';

import store from './store';

Vue.config.productionTip = false;
Vue.use(VueResource);
Vue.use(Vuex);

new Vue({
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
