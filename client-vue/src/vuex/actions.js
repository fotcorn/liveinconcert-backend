import Vue from 'vue'
import {LOAD_EVENTS} from './mutation-types'

export function loadEvents ({dispatch}) {
  Vue.http.get('http://localhost:8000/api/event/').then(response => {
    dispatch(LOAD_EVENTS, response.json())
  })
}

export function setEventRating ({dispatch}, eventId, rating) {
  // TODO
}
