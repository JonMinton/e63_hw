import { saveAs } from 'file-saver'



import React, { useState, useEffect, useRef } from 'react';


import "./XkcdBox.css"

const XkcdBox = () => {

    const [xkcds, setXkcds] = useState([])
    
    const [currentPage, setCurrentPage] = useState(1)
    const [maxPage, setMaxPage] = useState(0)

    // https://xkcd.com/2763/info.0.json

    useEffect( 
        () => {
            fetchLastComicJson()
        }, [] // This should happen once, on initalisation
    )

    useEffect(
        () => {

        }
    )

    useEffect(
        () => {
            fetchComicJson(currentPage)
        }, [maxPage] // This should happen once, after initialisation
    )

    useEffect(
        () => {
            fetchComicJson(currentPage)
        }, [xkcds] // This should happen many but not infinite times
    )

    const saveFileSoFar = (data) => {
        let blob = new Blob([JSON.stringify(data)], { type: 'application/json' })
        saveAs(blob, '/Users/JonMinton/e63_hw/wk_07/dy_5/xkcd_app/export.json')        
    } 



    const fetchComicJson = (page) => {
        fetch(`https://cors-anywhere.herokuapp.com/https://xkcd.com/${page}/info.0.json`)
            .then(res => {
                console.log(currentPage)
                if (res.ok) {
                    return res.json()
                }
                throw new Error("Something went wrong fetching - too many requests?")
            })
            .then(res => {
                setXkcds([...xkcds, res])
                setCurrentPage(currentPage + 1)
            })
            .then(() => {
                setTimeout(null, 500)
            })
            .catch((error) => {
                console.log(error, "on", currentPage)
                saveFileSoFar(xkcds)
                setTimeout(fetchComicJson, 10000)
            })
    }

    const fetchLastComicJson = () => {
        fetch('https://cors-anywhere.herokuapp.com/https://xkcd.com/info.0.json')
            // .then(res => console.log(res))
            .then(res => res.json())
            .then(res => {
                setMaxPage(res.num)
            })
            // .then(res => console.log(res.num))
    }

    const handleOnClick = () => {
        fetchComicJson(1);
    }

    const handleOnClickLatest = () => {
        fetchLastComicJson()
    }

    return (
        <div className = "XkcdBox">
            <h2>XkcdBox</h2>
            <p onClick={handleOnClick}>Click me to fetch all comics</p>
            <p onClick={handleOnClickLatest}>Click for last comic</p>
        </div>
      );
}
 
export default XkcdBox;