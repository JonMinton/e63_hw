const FilmBox = ({id, name, url}) => {
    return ( 
        <li key = {id}>
            <a href = {url}>{name}</a>
        </li>
    );
}
 
export default FilmBox;