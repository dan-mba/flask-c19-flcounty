import {createMuiTheme} from '@material-ui/core'

const theme = createMuiTheme({
  palette: {
    primary: {
      main: '#212121'
    },
    secondary: {
      main: '#004c7b'
    },
    background: {
      default: '#dbe3e8',
      paper: '#f1f4f6'
    },
    text: {
      secondary: '#004c7b'
    }
  },
  overrides: {
    MuiCssBaseline: {
      '@global': {
        body: {
          maxWidth: 1200,
          margin: '0 auto',
          padding: '1%'
        }
      }
    }
  }
});

export default theme;