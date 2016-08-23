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
      <tr>
        <td>Rammstein</td>
        <td>Sonisphere Luzern</td>
        <td>12.7.2016</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
  export default {
    methods: {
      clicked () {
        window.alert('clicked')
      }
    }
  }
</script>

<style lang="scss" scoped>
  table {
    width: 100%;
  }
</style>
