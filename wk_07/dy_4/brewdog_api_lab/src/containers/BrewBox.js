import React, {useEffect, useState } from 'react';


import FavouriteBeers from "../components/FavouriteBeers";
import HeaderBox from "../components/HeaderBox";
import SelectedBeer from "../components/SelectedBeer";
import AllBeers from "../components/AllBeers";
import InfoBox from "../components/InfoBox";

import './BrewBox.css';

const BrewBox = () => {

    const [beers, setBeers] = useState([])

    useEffect(() => {
        fetchBeers();
      }, [])




    const fetchBeers = function(){
        console.log("fetchBeers triggered")
        const urlToUse = "https://api.punkapi.com/v2/beers"

        fetch(urlToUse)
            .then(res => res.json())
            .then(res => {
                const fetchedBeersFull = res.map(({id, name}) => {
                    return (
                        {
                            id : id,
                            name : name
                        }
                    )
                })
            
                setBeers(fetchedBeersFull)
            })

    }




    return (
    <div className="BrewBox">
        <h2>BrewBox</h2>
        <HeaderBox />
        <SelectedBeer />
        <FavouriteBeers />
        <AllBeers beers = {beers}/>
        <InfoBox />
    </div>  );
}
 
export default BrewBox;