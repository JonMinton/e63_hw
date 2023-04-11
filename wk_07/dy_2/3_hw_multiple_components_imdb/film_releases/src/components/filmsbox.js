import FilmBox from "./filmbox";

const FilmsBox = ({films}) => {

    const filmItems = films.map(film => {
        return(
            <FilmBox id = {film.id} name = {film.name} url = {film.url} />
        )

    })

    return (
        <>
            {filmItems}
        </>  
    );
}
 
export default FilmsBox;