import * as types from './mutation-types'

export default {
  [types.LOAD_ARTISTS] (state, artists) {
    state.artists = artists
  },
  [types.LOAD_EVENTS] (state, events) {
    state.events = events
  },
  [types.SET_ARTIST_RATING] (state, artistId, rating) {
    state.artists[artistId].rating = rating
  },
  [types.SET_EVENT_RSVP] (state, eventId, rsvp) {
    state.events[eventId].rsvp = rsvp
  }
}
