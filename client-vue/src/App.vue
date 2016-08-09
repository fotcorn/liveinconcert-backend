<template>
  <div id="app" class="mdl-layout mdl-js-layout">
    <header class="mdl-layout__header mdl-layout__header--scroll">
      <div class="mdl-layout__header-row">
        <span class="mdl-layout-title">Live in Concert</span>
      </div>
    </header>
    <div class="mdl-layout__drawer">
      <span class="mdl-layout-title">Live in Concert</span>
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="">Upcoming Events</a>
        <a class="mdl-navigation__link" href="">Artists</a>
        <a class="mdl-navigation__link" href="">Locations</a>
      </nav>
    </div>
    <main class="mdl-layout__content">
      <div class="mdl-grid">
        <div class="mdl-cell mdl-cell--12-col">
          <hello></hello>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
  import Hello from './components/Hello'
  import 'material-design-lite'

  export default {
    components: {
      Hello
    }
  }
</script>

<style src="material-design-lite/dist/material.indigo-blue.min.css"></style>
<style src="material-design-icons/iconfont/material-icons.css"></style>
