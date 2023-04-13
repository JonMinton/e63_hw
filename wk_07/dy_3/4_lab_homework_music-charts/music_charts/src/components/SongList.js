import SongItem from "./SongItem"

const SongList = ({songs}) => {


    // const songItem1 = songs[0]
    // const songItems = songs.map((song, index) => {
    //         return (
    //             <SongItem 
    //                 key= {index} 
    //                 song = {song}
    //             />
    //             )
    //         }
    //     )



    return (
    <>
        <h3>I'm going to be a song list</h3>
        {songs ? <p>I agree there are {songs.length} songs</p> : null }
        <ol>
            {songs.map((song, index) => {
                return <SongItem song={song}/>
            })}
        </ol>


    </>
    );
}
 
export default SongList;