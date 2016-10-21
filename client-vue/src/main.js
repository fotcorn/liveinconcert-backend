import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

import EventList from './components/EventList'
import ArtistList from './components/ArtistList'
import Login from './components/Login'

import Auth from './services/auth'

Vue.use(VueRouter)
Vue.use(VueResource)

// routing
var router = new VueRouter({
  'history': true
})

router.map({
  '/': {
    component: EventList
  },
  '/artists': {
    component: ArtistList
  },
  '/login': {
    component: Login
  }
})

// authentication
router.beforeEach(function (transition) {
  if (Auth.isAuthenticated) {
    if (transition.to.path === '/login') {
      transition.redirect('/') // go to EventList when already logged in
    } else {
      transition.next()
    }
  } else {
    if (transition.to.path === '/login') {
      transition.next()
    } else {
      transition.redirect('/login')
    }
  }
})

Auth.checkAuth()

Vue.http.interceptors.push((request, next) => {
  next((response) => {
    if (response.status === 403) {
      Auth.deauth()
      router.go('/login')
    }
  })
})

// http/resource
Vue.http.options.root = 'http://localhost:8000/api'

// app startup
const App = Vue.extend(require('./components/App.vue'))
router.start(App, '#app')
