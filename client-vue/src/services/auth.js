import Vue from 'vue'

const JWT_LOCAL_STORAGE = 'jwt'

export default {
  isAuthenticated: false,

  login (context, username, password) {
    context.$http.post('http://localhost:8000/api-token-auth/', {'username': username, 'password': password}).then(({data}) => {
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

  _setToken (token) {
    Vue.http.headers.common['Authorization'] = 'JWT ' + token
  }
}
