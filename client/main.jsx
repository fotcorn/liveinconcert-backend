import React from 'react';
import ReactDOM from 'react-dom';

import AppBar from 'material-ui/lib/app-bar';
import MusicVideo from 'material-ui/lib/svg-icons/av/music-video';
import Colors from 'material-ui/lib/styles/colors';
import IconButton from 'material-ui/lib/icon-button';
import List from 'material-ui/lib/lists/list';
import ListItem from 'material-ui/lib/lists/list-item';
import Paper from 'material-ui/lib/paper';

import injectTapEventPlugin from 'react-tap-event-plugin';

injectTapEventPlugin();


const LICAppBar = () => (
  <AppBar title="Live in Concert" iconElementLeft={
    <IconButton>
      <MusicVideo color={Colors.white}/>
    </IconButton>
  }/>
);


class VenueList extends React.Component {
  render() {
    return <List>
      <ListItem primaryText="Inbox" />
      <ListItem primaryText="Starred" />
      <ListItem primaryText="Sent mail" />
      <ListItem primaryText="Drafts" />
      <ListItem primaryText="Inbox" />
    </List>
  }
}

const Page = () => (
  <div>
    <LICAppBar />
    <Paper style={{margin: 15}}>
      <VenueList />
    </Paper>
  </div>
);

ReactDOM.render(<Page/>, document.getElementById('hello'));
