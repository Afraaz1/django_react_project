import AnimeResults from '../components/AnimeResults';
import React, { useContext, useEffect, useState } from 'react';
import { QueryContext } from '../context/query';
import { Box, Typography} from '@material-ui/core'

const Results = () => {
    const query = useContext(QueryContext);
         
      return (
        <Box mt={2}>
          {(query.data.length > 0 && <AnimeResults data={query.animeData} />) || (
            <Typography>No Data Exists</Typography>
          )}
        </Box>
      );
    };
    

export default Results;