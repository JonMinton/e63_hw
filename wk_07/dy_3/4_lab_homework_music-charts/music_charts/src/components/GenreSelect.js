const GenreSelect = ({genreChangeHandler}) => {

    const genres = ['All', 'Rock', 'Dance', 'Country']

    const genreOptions = ({genres}) => {
        return  genres.map((genre) => {
            return (
                <option value={genre}>{genre}</option>
            )
        })
    }


    return (
    <>
        <h3>I'm going to select a genre</h3> 
        <select name = "genreSelect" id = "genreSelect">
            {genreOptions()}
        </select>    
    </>
    
    );
}
 
export default GenreSelect;