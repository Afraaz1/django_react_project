import React, { useContext, useEffect, useState } from 'react';
import { Typography } from '@material-ui/core';
import SingleAnime from '../components/SingleAnime';
import { QueryContext } from '../context/query';

const Single = () => {
  const search = useContext(QueryContext); //Query context to share methods
  const [dataExists, setDataExists] = useState(true); //Checking if data exists


  //Similar to results method, checks if data exists, and if it does passes it to return function if 
  //not passes an error
  useEffect(() => {
    if (
      search.singleData === undefined ||
      Object.keys(search.singleData).length === 0
    ) {
      try {
        search.setSingle(JSON.parse(localStorage.getItem('singleData')));
        setDataExists(true);
      } catch (error) {
        console.log(error);
        setDataExists(false);
      }
    }
  }, [search]);


  //display single anime using the single anime component 
  return (
    <div>
      {(dataExists && <SingleAnime info={search.singleData} />) || (
        <Typography>No data exists for this Anime</Typography>
      )}
    </div>
  );
};

export default Single;