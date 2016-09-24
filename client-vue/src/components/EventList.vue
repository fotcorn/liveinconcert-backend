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
            <button type="button" class="btn btn-success" v-bind:class="{'active': rsvp.rsvp == 1}" v-on:click="setEventRSVP(rsvp.id, 1)">
              <i class="fa fa-thumbs-up"></i>
            </button>
            <button type="button" class="btn btn-default" v-bind:class="{'active': rsvp.rsvp == 3}" v-on:click="setEventRSVP(rsvp.id, 3)">
              <i class="fa fa-question"></i>
            </button>
            <button type="button" class="btn btn-danger" v-bind:class="{'active': rsvp.rsvp == 2}" v-on:click="setEventRSVP(rsvp.id, 2)">
              <i class="fa fa-thumbs-down"></i>
            </button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
  import {loadEventRSVPs, setEventRSVP} from '../vuex/actions'

  export default {
    vuex: {
      actions: {
        loadEventRSVPs,
        setEventRSVP
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
