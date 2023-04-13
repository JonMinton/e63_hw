const GenreSelect = ({genres, setSelectedGenre}) => {

    const handleChange = function(e) {
        setSelectedGenre(genres[e.target.value])
    }


    const genreOptions = genres.map((genre, index) => {
        return <option value={index}>{genre}</option>
    })

    return (
    <>
        <h3>GenreSelect</h3>
        <select onChange = {handleChange}>
            {genreOptions}
        </select>  
    </>
    );
}
 
export default GenreSelect;