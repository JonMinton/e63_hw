const Song = ({song}) => {
    console.log(song)
    console.log(song["im:name"]["label"])
    return (
        <li>
            <a href = {song["id"]["label"]}>
                {song["im:name"]["label"]} by {song["im:artist"]["label"]}
            </a>
        </li>

    );
}
 
export default Song;