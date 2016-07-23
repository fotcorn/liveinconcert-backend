import React from 'react';
import ReactDOM from 'react-dom';

import AppBar from 'material-ui/lib/app-bar';
import MusicVideo from 'material-ui/lib/svg-icons/av/music-video';
import Colors from 'material-ui/lib/styles/colors';
import IconButton from 'material-ui/lib/icon-button';
import {Table, TableBody, TableHeader, TableHeaderColumn, TableRow, TableRowColumn} from 'material-ui/lib/table';
import Paper from 'material-ui/lib/paper';
import Check from 'material-ui/lib/svg-icons/navigation/check';
import Close from 'material-ui/lib/svg-icons/navigation/close';


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

  handleCheck() {
    alert('check');
  }
  handleClose() {
    alert('close');
  }


  render() {
    return <TableRow>
        <TableRowColumn>
          <div><a href={this.props.event.url} target="_blank">{this.props.event.artist.name} @ {this.props.event.name}</a></div>
          <div>{this.props.event.location}</div>
        </TableRowColumn>
        <TableRowColumn>
          <IconButton onClick={this.handleCheck}>
            <Check/>
          </IconButton>
          <IconButton onClick={this.handleClose}>
            <Close/>
          </IconButton>
        </TableRowColumn>
      </TableRow>
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
    return <Table>
    <TableBody displayRowCheckbox={false}>
      { this.state.events.map((event) => { return <VenueItem event={event} /> }) }
    </TableBody>
  </Table>
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
