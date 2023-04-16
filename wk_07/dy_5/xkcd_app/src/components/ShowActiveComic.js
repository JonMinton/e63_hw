import "./ShowActiveComic.css"

import React, {useState } from 'react';


const ShowActiveComic = ({comic}) => {

    const [showTooltip, setShowTooltip] = useState(false);
    const [showMoreInfo, setShowMoreInfo] = useState(false);
    const [tooltipPosition, setTooltipPosition] = useState({ x: 0, y: 0 });


  
    const handleMouseOver = (event) => {
      setShowTooltip(true);
      setTooltipPosition({ x: event.clientX, y: event.clientY });
    };
  
    const handleMouseOut = () => {
      setShowTooltip(false);
    };

    const handleOnClick = () => {
        console.log("Click registered");
        showMoreInfo ? setShowMoreInfo(false) : setShowMoreInfo(true);
    }

    const convertToDate = () => {
        return new Date (comic.year, comic.month - 1, comic.day)
    }

    const renderMoreInfo = () => {
        return (
            <>
                <ul>
                    <li><b>Number</b>: {comic.num} <b>Title</b>: {comic.title}</li>
                    <li><b>Alt</b>: {comic.alt}</li>
                    <li><b>Date</b>: The comic was published on {convertToDate().toDateString()}</li>
                </ul>
            </>
        )
    }

    return (
    <div className="ShowActiveComic">
        <h3>ShowActiveComic</h3>
        <img src = {comic.img} alt = {comic.alt} onClick = {handleOnClick} onMouseOver={handleMouseOver} onMouseOut={handleMouseOut}/>
        {showTooltip && (
        <div
          style={{
            position: 'absolute',
            left: tooltipPosition.x + 10,
            top: tooltipPosition.y + 10,
            backgroundColor: 'black',
            color: 'white',
            padding: '5px',
            borderRadius: '5px',
          }}
        >
          {comic.alt}
        </div>
      )}
      {showMoreInfo && renderMoreInfo()}
    </div>  
    );
}
 
export default ShowActiveComic;