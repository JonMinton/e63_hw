const SongItem = ({key, song}) => {
    return (<>
            <li>{song["im:name"]["label"]} by {song["im:artist"]["label"]}</li>           
    </> );
}
 
export default SongItem;