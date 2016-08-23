import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './components/App'
import EventList from './components/EventList'
import ArtistList from './components/ArtistList'

Vue.use(VueRouter)

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

router.start(App, 'body')
