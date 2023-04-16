import allXkcds from '/Users/JonMinton/e63_hw/wk_07/dy_5/xkcd_app/src/data/xkcds.json/allXkcds.json';


import React, { useState, useEffect} from 'react';

import "./XkcdBox.css"

import HeaderBox from '../components/HeaderBox';
import ComicsList from '../components/ComicsList';
import ShowActiveComic from '../components/ShowActiveComic';
import YearSelect from '../components/YearSelect';

const XkcdBox = () => {

    const [completeXkcds, setCompleteXkcds] = useState([])
    const [xkcds, setXkcds] = useState([])
    const [activeComic, setActiveComic] = useState(null)
    const [years, setYears] = useState([])


    useEffect(
        () => {
            setCompleteXkcds(allXkcds)
            console.log(`Initial useEffect call. Total collection of ${completeXkcds.length} elements`)
        },
        []
    )

    useEffect(
        () => {
            setXkcds(completeXkcds)
            console.log(`Second useEffect call. Subset collection of ${xkcds.length} elements`)
            const allYears = [...new Set(completeXkcds.map(comic => comic.year))]
            setYears(allYears)
        },
        [completeXkcds]
    )


    const changeActiveComic = (indx) => {
        setActiveComic(xkcds[indx])
    }

    const handleYearFilter = (yr) => {
        if (yr === "") {
            console.log("handleYearFilter called with all years")
            setXkcds(completeXkcds)
            setActiveComic(null)
        } else {
            console.log(`handleYearFilter called with year ${yr}`)
            const subsetComics = completeXkcds.filter(comic => comic.year === yr)
            setXkcds(subsetComics)
            setActiveComic(null)
        }
    }

    return (
        <div className = "XkcdBox">
            <HeaderBox/>
            <h2>XkcdBox</h2>
            <p> There are {xkcds.length} elements in the array</p>
            <ComicsList comics = {xkcds} changeActiveComic={changeActiveComic}/>
            <YearSelect years = {years} handleYearFilter = {handleYearFilter}/>
            {activeComic && <p>Active comic name: {activeComic.title}</p>}
            {activeComic && <ShowActiveComic comic={activeComic}/> }  
        </div>
      );
}
 
export default XkcdBox;