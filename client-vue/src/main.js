import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

import EventList from './components/EventList'
import ArtistList from './components/ArtistList'

Vue.use(VueRouter)
Vue.use(VueResource)

var router = new VueRouter({
  'history': true
})

router.map({
  '/': {
    component: EventList
  },
  '/artists': {
    component: ArtistList
  }
})

const App = Vue.extend(require('./components/App.vue'))
router.start(App, '#app')
