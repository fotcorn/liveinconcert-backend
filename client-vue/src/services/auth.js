import Vue from 'vue'

const JWT_LOCAL_STORAGE = 'jwt'

export default {
  isAuthenticated: false,

  login (context, username, password) {
    context.$http.post('auth/', {'username': username, 'password': password}).then(({data}) => {
      let token = data.token
      window.localStorage.setItem(JWT_LOCAL_STORAGE, token)
      this._setToken(token)
      this.isAuthenticated = true
      context.$router.go('/')
    })
  },

  checkAuth () {
    var token = window.localStorage.getItem(JWT_LOCAL_STORAGE)
    if (token) {
      this._setToken(token)
      this.isAuthenticated = true
    } else {
      this.isAuthenticated = false
    }
  },

  deauth () {
    this.isAuthenticated = false
    window.localStorage.removeItem(JWT_LOCAL_STORAGE)
  },

  _setToken (token) {
    Vue.http.headers.common['Authorization'] = 'JWT ' + token
  }
}
