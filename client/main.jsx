import React from 'react';
import ReactDOM from 'react-dom';

import AppBar from 'material-ui/lib/app-bar';
import MusicVideo from 'material-ui/lib/svg-icons/av/music-video';
import Colors from 'material-ui/lib/styles/colors';
import IconButton from 'material-ui/lib/icon-button';

import injectTapEventPlugin from 'react-tap-event-plugin';

injectTapEventPlugin();


const LICAppBar = () => (
  <AppBar title="Live in Concert" iconElementLeft={
    <IconButton>
      <MusicVideo color={Colors.white}/>
    </IconButton>
  }/>
);

class Page extends React.Component {
  render() {
    return <div>
      <LICAppBar />
      <h1>Hello World</h1>
    </div>
  }
}
 
ReactDOM.render(<Page/>, document.getElementById('hello'));
