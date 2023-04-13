import Song from "./Song";

const SongsList = ({songs}) => {

    const renderSongItems = () => {
        return songs.map( (song, index) => {
            return <Song key = {index} song = {song} />
        })
    }
    return (
    <>
        <h3>SongsList</h3>
        <p>There are {songs.length} songs</p>
        <ol>
            {renderSongItems()}
        </ol>

    </>
  );
}
 
export default SongsList;