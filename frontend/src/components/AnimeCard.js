import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { QueryContext } from '../context/query';
import { Typography, Link, Paper, GridListTile, Grid } from '@material-ui/core';
import './AnimeCard.scss';

const AnimeCard = (props) => {
  const navigation = useNavigate();

  const query = useContext(QueryContext);

  const onClickHandler = (event) => {
    event.preventDefault();
    fetch(`https://api.jikan.moe/v3/anime/${props.anime.mal_id}`)
      .then((response) => response.json())
      .then((data) => {
        query.setSingle(data);
        localStorage.setItem('singleData', JSON.stringify(data));
        navigation('/single');
      });
  };

  const title =
    props.anime.title.length > 20
      ? `${props.anime.title.substring(0, 15)}...`
      : props.anime.title;
  const imageUrl = props.anime.image_url;
  const synopsis =
    props.anime.synopsis.length > 30
      ? `${props.anime.synopsis.substring(0, 30)}...`
      : props.anime.synopsis;

  return (
    <GridListTile className="animecard__container">
      <Grid container item xs={12}>
        <Paper className="animecard__paper">
          <img src={imageUrl} alt={title} style={{ maxHeight: 300 }} />
          <Typography variant="h5" component="h2">
            {title}
          </Typography>
          <Typography variant="body2" component="h2" paragraph={true}>
            {synopsis}
          </Typography>
          <Link
            component="button"
            variant="body1"
            style={{ marginBottom: 0 }}
            onClick={onClickHandler}
          >
            Recommend me something similar to this!
          </Link>
        </Paper>
      </Grid>
    </GridListTile>
  );
};

export default AnimeCard;