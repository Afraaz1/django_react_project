import React, { useContext, useState } from 'react';
import { useNavigate } from "react-router-dom";
import { QueryContext } from '../context/query';
import { FormControl, IconButton, Grid } from '@mui/material';
import Input from '@mui/material/Input';
import SearchIcon from '@mui/icons-material/Search';
import { height } from '@mui/system';
import './Home.scss';


const Home = () => {
    let navigate = useNavigate(); //Lets home page send user to another page
    const query = useContext(QueryContext) //Calls query context 
    const [input, setInput] = useState('') //Setting input for search function

//Handles any input put into the search bar
const handleQuery = (event) => {
    event.preventDefault();
    query.query(input).then((data) => 
        {
        console.log(data)
        query.setData(data.results)

        //Saves data to local storage to ensure that refreshing doesn't erase everything
        localStorage.setItem('myData', JSON.stringify(data.results));

        //Sends user to another page
        navigate('/Results'); 
    });  
    };
    
    //Displaying home page image and search bar
    return <Grid 
    container direction="column" 
    justify="center" 
    alignContent="center" 
    alignItems ="center"
    >
        <Grid item>
            <Grid item> 
            <img
            alt="mountains"
            src={process.env.PUBLIC_URL + '/mountains.png'} 
            height={550}
            width={1200}
            />
            </Grid>
            <Grid search>
                <form className="form">
                    <FormControl type="submit" className="formControl" >
                        <Input 
                        placeholder="What anime do you want a recommendation for?" 
                        value={input} 
                        onChange={(event) => setInput(event.target.value)}
                        className = "input"
                        />
                        <IconButton 
                        className = "icon"
                        variant="contained" 
                        type="submit" 
                        disabled={!input} 
                        onClick={handleQuery}>
                            <SearchIcon/>
                        </IconButton>
                    </FormControl>
                </form>
            </Grid>
        </Grid>
    </Grid>
};

export default Home;