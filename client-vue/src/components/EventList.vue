<template>
  <h1>Events</h1>
  <table class="table">
    <tbody>
      <tr v-for="rsvp in rsvps">
        <td>
          <b>{{ rsvp.event.artist.name }}</b><br>
          {{ rsvp.event.location }}<br>
          {{ rsvp.event.date_time }}
        </td>
        <td>
          <div class="btn-group">
            <button type="button" class="btn btn-success">
              <i class="fa fa-thumbs-up"></i>
            </button>
            <button type="button" class="btn btn-default">
              <i class="fa fa-question"></i>
            </button>
            <button type="button" class="btn btn-danger">
              <i class="fa fa-thumbs-down"></i>
            </button>
          </div>
        </td>
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
