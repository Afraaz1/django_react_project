import React, {useState} from 'react';
import {BrowserRouter as Router, 
  Route, 
  Routes, 
  Navigate 
} from 'react-router-dom';
import Home from'./pages/Home';
import Recommend from'./pages/Recommend';
import Single from'./pages/Single';
import Results from'./pages/Results';
import MainNavigation from './components/MainNavigation';
import {QueryContext} from './context/query'
import axios from 'axios';


function App() {

  //Setting up methods to store data using use states
  const [animeData, setAnimeData] = useState([]); 
  const [singleData, setSingleData] = useState({});
  

  //Saving data
  const setData = (data) => {
    setAnimeData(data)
  };

  //Setting data for a single anime when a user clicks on an anime
  const setSingle = (data) => {
    setSingleData(data)
  };

  //API look up function
  const query = (anime) => {
    return fetch(
      `http://localhost:8000/anime.${anime}`
    ).then((response) => response.json());
  }
  //Handling all routing, routes everything that isn't a specified URL to home page
  return (
    //Causes query context methods to be available everywhere in the program without importing 
    <QueryContext.Provider 
    value = {{ query, animeData, setData, singleData, setSingle}}>
    <Router>
      <main>
        <MainNavigation/>
        <Routes>
          <Route path="/home" element={<Home />}>
          </Route>
          <Route path="/Recommend" 
          element={<Recommend />}>
          </Route>
          <Route path="/Single" 
          element={<Single />}>
          </Route>
          <Route path="/Results" 
          element={<Results />}>
          </Route>
          <Route element={<Navigate replace to ="/home" />}/>
        </Routes>
      </main>
    </Router>
    </QueryContext.Provider>
  );
}

export default App;
