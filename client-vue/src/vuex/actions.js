import Vue from 'vue'
import {LOAD_EVENT_RSVPS} from './mutation-types'

export function loadEventRSVPs ({dispatch}) {
  Vue.http.get('eventrsvp/').then(response => {
    dispatch(LOAD_EVENT_RSVPS, response.json())
  })
}

export function setEventRSVP ({dispatch}, rsvpId, rating) {
  // TODO
}
