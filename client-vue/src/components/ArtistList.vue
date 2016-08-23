<template>
  <h1>Artists</h1>
  <table class="table">
    <thead>
      <tr>
        <th>Artist</th>
        <th>Like/Dont Like</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Rammstein</td>
        <td>Like</td>
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
