import React from 'react';
import AnimeCard from './AnimeCard';
import { GridList } from '@material-ui/core';

const AnimeResults = (props) => {
  //Maps data from every array onto an anime card
  return (
    <GridList className="animelist__container">
      {props.data.map((anime) => (
        <AnimeCard key={anime.anime_id} anime={anime} />
      ))}
    </GridList>
  );
};

export default AnimeResults;