<template>
  <nav class="navbar navbar-default navbar-inverse navbar-static-top">
    <div class="container">
      <!-- Brand and toggle get grouped for better mobile display -->
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <span class="navbar-brand">Live in Concert</span>
      </div>
      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
          <li><a v-link="{ path: '/' }">Events</a></li>
          <li><a v-link="{ path: '/artists' }">Artists</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <div class="container">
    <div class="row">
      <div class="col-sm-12">
          <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<style src="bootstrap/dist/css/bootstrap.css"></style>
