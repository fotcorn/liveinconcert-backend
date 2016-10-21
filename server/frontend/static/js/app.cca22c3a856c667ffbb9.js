webpackJsonp([2,0],[function(t,e,s){"use strict";function n(t){return t&&t.__esModule?t:{"default":t}}var o=s(2),a=n(o),r=s(44),i=n(r),l=s(43),u=n(l),d=s(41),c=n(d),v=s(40),p=n(v),f=s(42),_=n(f),b=s(4),h=n(b);a["default"].use(i["default"]),a["default"].use(u["default"]);var m=new i["default"]({history:!0});m.map({"/":{component:c["default"]},"/artists":{component:p["default"]},"/login":{component:_["default"]}}),m.beforeEach(function(t){h["default"].isAuthenticated?"/login"===t.to.path?t.redirect("/"):t.next():"/login"===t.to.path?t.next():t.redirect("/login")}),h["default"].checkAuth(),a["default"].http.interceptors.push(function(t,e){e(function(t){403===t.status&&(h["default"].deauth(),m.go("/login"))})}),a["default"].http.options.root="https://concert.9a.io/api";var x=a["default"].extend(s(39));m.start(x,"#app")},,,,function(t,e,s){"use strict";function n(t){return t&&t.__esModule?t:{"default":t}}Object.defineProperty(e,"__esModule",{value:!0});var o=s(2),a=n(o),r="jwt";e["default"]={isAuthenticated:!1,login:function(t,e,s){var n=this;t.$http.post("auth/",{username:e,password:s}).then(function(e){var s=e.data,o=s.token;window.localStorage.setItem(r,o),n._setToken(o),n.isAuthenticated=!0,t.$router.go("/")})},checkAuth:function(){var t=window.localStorage.getItem(r);t?(this._setToken(t),this.isAuthenticated=!0):this.isAuthenticated=!1},deauth:function(){this.isAuthenticated=!1,window.localStorage.removeItem(r)},_setToken:function(t){a["default"].http.headers.common.Authorization="JWT "+t}}},function(t,e){"use strict";Object.defineProperty(e,"__esModule",{value:!0});e.LOAD_ARTISTS="LOAD_ARTISTS",e.LOAD_EVENT_RSVPS="LOAD_EVENT_RSVPS",e.SET_ARTIST_RATING="SET_ARTIST_RATING",e.SET_EVENT_RSVP="SET_EVENT_RSVP"},,,,,function(t,e,s){"use strict";function n(t){return t&&t.__esModule?t:{"default":t}}function o(t){var e=t.dispatch;i["default"].http.get("eventrsvp/").then(function(t){e(l.LOAD_EVENT_RSVPS,t.json())})}function a(t,e,s){var n=t.dispatch;n(l.SET_EVENT_RSVP,e,s)}Object.defineProperty(e,"__esModule",{value:!0}),e.loadEventRSVPs=o,e.setEventRSVP=a;var r=s(2),i=n(r),l=s(5)},function(t,e,s){"use strict";function n(t){if(t&&t.__esModule)return t;var e={};if(null!=t)for(var s in t)Object.prototype.hasOwnProperty.call(t,s)&&(e[s]=t[s]);return e["default"]=t,e}function o(t){return t&&t.__esModule?t:{"default":t}}Object.defineProperty(e,"__esModule",{value:!0});var a,r=s(18),i=o(r),l=s(5),u=n(l);e["default"]=(a={},(0,i["default"])(a,u.LOAD_ARTISTS,function(t,e){t.artists=e}),(0,i["default"])(a,u.LOAD_EVENT_RSVPS,function(t,e){t.rsvps=e}),(0,i["default"])(a,u.SET_ARTIST_RATING,function(t,e,s){t.artists[e].rating=s}),(0,i["default"])(a,u.SET_EVENT_RSVP,function(t,e,s){}),a)},function(t,e,s){"use strict";function n(t){return t&&t.__esModule?t:{"default":t}}Object.defineProperty(e,"__esModule",{value:!0});var o=s(2),a=n(o),r=s(45),i=n(r),l=s(11),u=n(l);a["default"].use(i["default"]);var d={artists:{},rsvps:{}};e["default"]=new i["default"].Store({state:d,mutations:u["default"]})},function(t,e,s){"use strict";function n(t){return t&&t.__esModule?t:{"default":t}}Object.defineProperty(e,"__esModule",{value:!0});var o=s(12),a=n(o);e["default"]={store:a["default"]}},function(t,e){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e["default"]={methods:{clicked:function(){window.alert("clicked")}}}},function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=s(10);e["default"]={vuex:{actions:{loadEventRSVPs:n.loadEventRSVPs,setEventRSVP:n.setEventRSVP},getters:{rsvps:function(t){return t.rsvps}}},created:function(){this.loadEventRSVPs()}}},function(t,e,s){"use strict";function n(t){return t&&t.__esModule?t:{"default":t}}Object.defineProperty(e,"__esModule",{value:!0});var o=s(4),a=n(o);e["default"]={data:function(){return{username:"",password:""}},methods:{login:function(){a["default"].login(this,this.username,this.password)}}}},,,,,,,,,,,,,,function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e){t.exports=' <div> <nav class="navbar navbar-default navbar-inverse navbar-static-top"> <div class=container> <div class=navbar-header> <button type=button class="navbar-toggle collapsed" data-toggle=collapse data-target=#bs-example-navbar-collapse-1 aria-expanded=false> <span class=sr-only>Toggle navigation</span> <span class=icon-bar></span> <span class=icon-bar></span> <span class=icon-bar></span> </button> <span class=navbar-brand>Live in Concert</span> </div> <div class="collapse navbar-collapse" id=bs-example-navbar-collapse-1> <ul class="nav navbar-nav"> <li><a v-link="{ path: \'/\' }">Events</a></li> <li><a v-link="{ path: \'/artists\' }">Artists</a></li> </ul> </div> </div> </nav> <div class=container> <div class=row> <div class=col-sm-12> <router-view></router-view> </div> </div> </div> </div> '},function(t,e){t.exports=' <h1>Login</h1> <form class=form-horizontal v-on:submit.prevent=login> <div class=form-group> <label for=username class="col-sm-2 control-label">Username</label> <div class=col-sm-10> <input type=text class=form-control id=username placeholder=Username v-model=username> </div> </div> <div class=form-group> <label for=password class="col-sm-2 control-label">Password</label> <div class=col-sm-10> <input type=password class=form-control id=password placeholder=Password v-model=password> </div> </div> <div class=form-group> <div class="col-sm-offset-2 col-sm-10"> <button class="btn btn-default">Sign in</button> </div> </div> </form> '},function(t,e){t.exports=' <h1 _v-22861946="">Events</h1> <table class=table _v-22861946=""> <tbody _v-22861946=""> <tr v-for="rsvp in rsvps" _v-22861946=""> <td _v-22861946=""> <b _v-22861946="">{{ rsvp.event.artist.name }}</b><br _v-22861946=""> {{ rsvp.event.location }}<br _v-22861946=""> {{ rsvp.event.date_time }} </td> <td _v-22861946=""> <div class=btn-group _v-22861946=""> <button type=button class="btn btn-success" v-bind:class="{\'active\': rsvp.rsvp == 1}" v-on:click="setEventRSVP(rsvp.id, 1)" _v-22861946=""> <i class="fa fa-thumbs-up" _v-22861946=""></i> </button> <button type=button class="btn btn-default" v-bind:class="{\'active\': rsvp.rsvp == 3}" v-on:click="setEventRSVP(rsvp.id, 3)" _v-22861946=""> <i class="fa fa-question" _v-22861946=""></i> </button> <button type=button class="btn btn-danger" v-bind:class="{\'active\': rsvp.rsvp == 2}" v-on:click="setEventRSVP(rsvp.id, 2)" _v-22861946=""> <i class="fa fa-thumbs-down" _v-22861946=""></i> </button> </div> </td> </tr> </tbody> </table> '},function(t,e){t.exports=' <h1 _v-4ad139f2="">Artists</h1> <table class=table _v-4ad139f2=""> <thead _v-4ad139f2=""> <tr _v-4ad139f2=""> <th _v-4ad139f2="">Artist</th> <th _v-4ad139f2="">Like/Dont Like</th> </tr> </thead> <tbody _v-4ad139f2=""> <tr _v-4ad139f2=""> <td _v-4ad139f2="">Rammstein</td> <td _v-4ad139f2="">Like</td> </tr> </tbody> </table> '},function(t,e,s){var n,o;s(30),s(31),s(32),n=s(13),o=s(35),t.exports=n||{},t.exports.__esModule&&(t.exports=t.exports["default"]),o&&(("function"==typeof t.exports?t.exports.options||(t.exports.options={}):t.exports).template=o)},function(t,e,s){var n,o;s(34),n=s(14),o=s(38),t.exports=n||{},t.exports.__esModule&&(t.exports=t.exports["default"]),o&&(("function"==typeof t.exports?t.exports.options||(t.exports.options={}):t.exports).template=o)},function(t,e,s){var n,o;s(33),n=s(15),o=s(37),t.exports=n||{},t.exports.__esModule&&(t.exports=t.exports["default"]),o&&(("function"==typeof t.exports?t.exports.options||(t.exports.options={}):t.exports).template=o)},function(t,e,s){var n,o;n=s(16),o=s(36),t.exports=n||{},t.exports.__esModule&&(t.exports=t.exports["default"]),o&&(("function"==typeof t.exports?t.exports.options||(t.exports.options={}):t.exports).template=o)}]);
//# sourceMappingURL=app.cca22c3a856c667ffbb9.js.map