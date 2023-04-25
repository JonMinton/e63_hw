import { useState, useEffect } from "react";

import './App.css';

import SightingsForm from "./SightingsForm";
import SightingsGrid from "./SightingsGrid";
import { getSightings, deleteSighting } from "./SightingService";

function App() {

  const [birdSightings, setBirdSightings] = useState([]);

  useEffect(() => {
    getSightings().then((allSightings) => {
      setBirdSightings(allSightings);
    })
  }, []);





  const addSighting = (sighting) => {
    setBirdSightings([...birdSightings, sighting]);
  }



  const removeSighting = (id) => {
    deleteSighting(id)
    .then( () => {
      let temp = birdSightings.map(s => s);
      const toDel = birdSightings.map( s => s._id).indexOf(id)
      temp.splice(toDel, 1)
      setBirdSightings(temp)
    })
  }




  return (
    <>
      <SightingsForm addSighting={addSighting} />
      <SightingsGrid sightings={birdSightings} removeSighting={removeSighting} />
    </>
  );
}

export default App;
