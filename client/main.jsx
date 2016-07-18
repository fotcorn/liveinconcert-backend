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


class VenueItem extends React.Component {
  constructor() {
    super();
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    window.open(this.props.event.url);
  }
  render() {
   return <ListItem primaryText={this.props.event.name + " @ " + this.props.event.location} onClick={this.handleClick}/>
  }
}

class VenueList extends React.Component {

  constructor(props) {
    super(props);
    this.state = {events: []}
  }

  componentDidMount() {
    fetch('http://10.0.0.27:8000/api/event/')
    .then((response) => {
      return response.json()
    }).then((json) => {
      this.setState({events: json});
    }).catch((ex) => {
      console.log('parsing failed', ex)
    });
  }

  render() {
    return <List>
      { this.state.events.map((event) => { return <VenueItem event={event} /> }) }
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
