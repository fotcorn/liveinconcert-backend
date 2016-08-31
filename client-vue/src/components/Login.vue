<template>
  <h1>Login</h1>
  <form class="form-horizontal" v-on:submit.prevent="login">
    <div class="form-group">
      <label for="username" class="col-sm-2 control-label">Username</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="username" placeholder="Username" v-model="username">
      </div>
    </div>
    <div class="form-group">
      <label for="password" class="col-sm-2 control-label">Password</label>
      <div class="col-sm-10">
        <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-offset-2 col-sm-10">
        <button class="btn btn-default">Sign in</button>
      </div>
    </div>
  </form>
</template>

<script>
  import Auth from '../services/auth.js'

  export default {
    data () {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      login () {
        Auth.login(this, this.username, this.password)
      }
    }
  }
</script>
