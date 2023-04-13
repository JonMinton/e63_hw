

import React, { useEffect, useState } from 'react';

import HeaderBox from "../components/HeaderBox";
import SongsList from "../components/SongsList";
import InfoBox from "../components/InfoBox";
import GenreSelect from '../components/GenreSelect';


const ChartsBox = () => {

    const genres = ["All", "Rock", "Dance", "Country"]
    const urlLookup = {
        'All' : "https://itunes.apple.com/gb/rss/topsongs/limit=20/json",
        'Rock' : "https://itunes.apple.com/gb/rss/topsongs/limit=20/genre=21/json",
        'Dance' : "https://itunes.apple.com/gb/rss/topsongs/limit=20/genre=17/json",
        'Country' : "https://itunes.apple.com/gb/rss/topsongs/limit=20/genre=6/json",
    }


    const [songs, setSongs] = useState([])
    const [genre, setGenre] = useState("All")
    

    useEffect(() => {
        fetchSongs();
      }, [])

    useEffect(() => {
        fetchSongs();
    }, [genre])


    const fetchSongs = function(){
        const urlToUse = urlLookup[genre]
        fetch(urlToUse)
            .then(res => res.json())
            .then(res => res.feed.entry) 
            .then(res => setSongs(res))
    }

    const setSelectedGenre = (selectedGenre) => {
        setGenre(selectedGenre)
    }

    return (
    <>
        <h2>ChartsBox</h2> 
        <GenreSelect genres = {genres} setSelectedGenre={setSelectedGenre}/> 
        <HeaderBox/>
        {songs ? <SongsList songs={songs}/> : null}
        <InfoBox/>
    </>
    );
}
 
export default ChartsBox;