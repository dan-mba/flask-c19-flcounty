import React, { useEffect, useState } from 'react';
import { ThemeProvider, CssBaseline, Grid, Typography, makeStyles } from '@material-ui/core';
import axios from 'axios';
import CountySelect from './components/CountySelect';
import theme from './util/theme';

const useStyles = makeStyles({
  img: {
    display: 'block',
    maxWidth: '100%'
  },
  grid: {
    margin: '20px auto',
    width: '98%'
  }
})

function App() {
  const [data, setData] = useState({sum: "", count: ""});
  const [county, setCounty] = useState()
  const classes = useStyles();

  useEffect(() => {
    if (!Number.isInteger(county)) return;

    axios(`./api/${county}`)
      .then((json) => {
        setData(json.data);
      })
  }, [county])

  return (
    <ThemeProvider theme={theme}>
      <React.Fragment>
        <CssBaseline />
        <Typography
          align="center"
          color="secondary"
          variant="h4"
        >Florida Covid-19 Cases By County</Typography>
        <CountySelect value={county} onChange={(e) => setCounty(Number(e.target.value))} />
        <Grid container spacing={2} classes={{root: classes.grid}}>
          { !data.sum ? null :
            <Grid item sm={12} md={6}>
              <Typography
                color="textPrimary"
                align="center"
                variant="h5"
              >Total Cases</Typography>
              <img src={data.sum} className={classes.img} alt="Total Cases"/>
            </Grid>
          }
          { !data.count ? null :
            <Grid item sm={12} md={6}>
              <Typography
                color="textPrimary"
                align="center"
                variant="h5"
              >New Cases</Typography>
              <img src={data.count} className={classes.img} alt="New Cases"/>
            </Grid>
          }
        </Grid>
      </React.Fragment>
    </ThemeProvider>
  );
}

export default App;
