import AnimeResults from '../components/AnimeResults';
import React, { useContext, useEffect, useState } from 'react';
import { QueryContext } from '../context/query';
import { Box, Typography} from '@material-ui/core'

const Results = () => {
    const query = useContext(QueryContext);
    const [dataExists, setDataExists] = useState(true);

    useEffect(() => {
        console.log(query.animeData)
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

      return (
        <Box mt={2}>
          {(dataExists && <AnimeResults data={query.animeData} />) || (
            <Typography>No Data Exists</Typography>
          )}
        </Box>
      );
    };
    

export default Results;