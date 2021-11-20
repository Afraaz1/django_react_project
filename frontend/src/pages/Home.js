import React, { useContext, useState } from 'react';
import { QueryContext } from '../context/query';
import { FormControl, IconButton, Grid } from '@mui/material';
import Input from '@mui/material/Input';
import SearchIcon from '@mui/icons-material/Search';
import { height } from '@mui/system';

const Home = () => {
    const query = useContext(QueryContext)
    const [input, setInput] = useState('')

    const handleQuery = (event) => {
        event.preventDefault();
    }
    

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
                <form>
                    <FormControl type="submit">
                        <Input placeHolder="What anime do you want a recommendation for?" 
                        value={input} 
                        onChange={(event) => setInput(event.target.value)}
                        />
                        <IconButton variant="contained" 
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