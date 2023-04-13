import React, {useEffect, useState } from 'react';


import FavouriteBeers from "../components/FavouriteBeers";
import HeaderBox from "../components/HeaderBox";
import SelectedBeer from "../components/SelectedBeer";
import AllBeers from "../components/AllBeers";
import InfoBox from "../components/InfoBox";

import './BrewBox.css';

const BrewBox = () => {

    const [beers, setBeers] = useState([])
    const [favouriteBeers, setFavouriteBeers] = useState([])
    const [selectedBeer, setSelectedBeer] = useState([])

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
                            name : name,
                            favourite : false
                        }
                    )
                })
            
                setBeers(fetchedBeersFull)
            })
    }

    const handleToggleBeerFavourited = function(id) {
        console.log("handleToggleBeerFavourited triggered")
        const beerToFocusOn = beers.find(beer => beer.id === id)
        const indexOfBeerToFocusOn = beers.findIndex(beer => beer.id === id)
        console.log(`The beer to toggle favourite status is ${beerToFocusOn.name}`)

        let tempBeers = [...beers];
        const favStatus = beerToFocusOn.favourite

        favStatus ? beerToFocusOn.favourite = false : beerToFocusOn.favourite = true

        tempBeers[indexOfBeerToFocusOn] = beerToFocusOn;
        setBeers(tempBeers)

        if (!favStatus) {
            let tempFavouriteBeers = [...favouriteBeers]
            tempFavouriteBeers.push(beerToFocusOn)
            setFavouriteBeers(tempFavouriteBeers)
        } else {
            let tempFavouriteBeers = [...favouriteBeers]
            tempFavouriteBeers.pop(tempFavouriteBeers.findIndex(beer => beer.id === id))
            setFavouriteBeers(tempFavouriteBeers)
        }

    }

    const handleSelectBeer = function(beer){
        console.log("handleSelectBeer toggled")
    }


    return (
    <div className="BrewBox">
        <h2>BrewBox</h2>
        <HeaderBox />
        <SelectedBeer selectedBeer = {selectedBeer}/>
        <FavouriteBeers 
            beers = {favouriteBeers}
            handleToggleBeerFavourited = {handleToggleBeerFavourited}
            handleSelectBeer = {handleSelectBeer}
        />
        <AllBeers 
            beers = {beers} 
            handleToggleBeerFavourited = {handleToggleBeerFavourited}
            handleSelectBeer = {handleSelectBeer}
        />
        <InfoBox />
    </div>  
    );
}
 
export default BrewBox;