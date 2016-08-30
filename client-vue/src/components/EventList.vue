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
      <tr v-for="event in events">
        <td>{{ event.artist.name }}</td>
        <td>{{ event.location }}</td>
        <td>{{ event.date_time }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
  import {loadEvents, setEventRating} from '../vuex/actions'

  export default {
    vuex: {
      actions: {
        loadEvents,
        setEventRating
      },
      getters: {
        events (state) {
          return state.events
        }
      }
    },
    created () {
      this.loadEvents()
    }
  }
</script>

<style lang="scss" scoped>
  table {
    width: 100%;
  }
</style>
