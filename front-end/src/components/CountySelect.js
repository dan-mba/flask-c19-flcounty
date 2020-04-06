import React from 'react';
import {NativeSelect, FormControl, InputLabel, makeStyles}
  from '@material-ui/core';
import COUNTIES from '../util/counties';

const useStyles = makeStyles({
  root:{
    display: 'flex',
    justifyContent: 'center'
  },
  resize: {
    fontSize: '1.25rem'
  }
})

export default function CountySelect({ value, onChange}) {
  const classes = useStyles();
  const label = "County";
  const options = COUNTIES.map((county, index) => 
    <option value={index} key={county}>
      {county.split(" ").map(c => c[0].toUpperCase() + c.slice(1)).join(" ")}
    </option>
  );

  return (
    <div className={classes.root}>
      <FormControl>
        <InputLabel htmlFor={label} classes={{root: classes.resize}}>{label}</InputLabel>
        {Number.isInteger(value)  ? 
          <NativeSelect
            value={value} 
            inputProps={{
              name: label,
              id: label
            }}
            onChange={onChange}
          >
            <option value=""></option>
            {options}
          </NativeSelect> : 
          <NativeSelect
            inputProps={{
              name: label,
              id: label
            }}
            onChange={onChange}
          >
            <option value=""></option>
            {options}
          </NativeSelect>
        }
      </FormControl>
    </div>
    )
}