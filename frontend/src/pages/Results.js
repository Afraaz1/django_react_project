import AnimeResults from '../components/AnimeResults';
import React, { useContext, useEffect, useState } from 'react';
import { QueryContext } from '../context/query';
import { Box, Typography} from '@material-ui/core'

//Page to display results after a user searches
const Results = () => {
  const query = useContext(QueryContext); //Calling query methods to save data
  const [dataExists, setDataExists] = useState(true); //Checking if data exists


  //Checks if search data exists, if it doesn't passes an error
  useEffect(() => {
    if (query.animeData === undefined || query.animeData.length === 0) {
      try {
        query.setData(JSON.parse(localStorage.getItem('myData')));
        setDataExists(true);
      } catch (error) {
        console.log(error);
        setDataExists(false);
      }
    }
  }, [query]);
      //Formats search data using single anime card components for each anime
      return (
        <Box mt={2}>
          {(dataExists && <AnimeResults data={query.animeData} />) || (
            <Typography>No Data Exists</Typography>
          )}
        </Box>
      );
    };
    

export default Results;