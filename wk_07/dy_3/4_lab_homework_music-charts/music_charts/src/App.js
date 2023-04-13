import {useState, useEffect} from "react";
import './App.css';
import SongsContainer from "./containers/SongsContainer";

function App() {

  const [songs, setSongs] = useState(null);
  const [url, setUrl] = useState("https://itunes.apple.com/gb/rss/topsongs/limit=20/json")
  const [genre, setGenre] = useState("all")


  useEffect(() => {
    fetchSongs();
  }, [])

  const fetchSongs =  function() {
      console.log("fetchSongs called")

    fetch(url)
    .then(response => response.json())
    .then(data => setSongs(data.feed.entry))
  }


  return (
    <>
      <h1>I'm a useless app</h1>
      {songs ? <SongsContainer songs = {songs}/> : null }
    </>
  );
}

export default App;
