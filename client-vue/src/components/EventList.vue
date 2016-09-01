<template>
  <h1>Events</h1>
  <table class="table">
    <thead>
      <tr>
        <th>Artist</th>
        <th>Event</th>
        <th>Date</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="rsvp in rsvps">
        <td>{{ rsvp.event.artist.name }}</td>
        <td>{{ rsvp.event.location }}</td>
        <td>{{ rsvp.event.date_time }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
  import {loadEventRSVPs, setEventRating} from '../vuex/actions'

  export default {
    vuex: {
      actions: {
        loadEventRSVPs,
        setEventRating
      },
      getters: {
        rsvps (state) {
          return state.rsvps
        }
      }
    },
    created () {
      this.loadEventRSVPs()
    }
  }
</script>

<style lang="scss" scoped>
  table {
    width: 100%;
  }
</style>
