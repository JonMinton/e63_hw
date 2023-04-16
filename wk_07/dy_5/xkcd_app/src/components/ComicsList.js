import './ComicsList.css'

const ComicsList = ({comics, changeActiveComic}) => {

    const renderComicOption = () => {
        return comics.map((comic, index) => {
            return (
                <option key = {index} value = {index}>{comic.title}</option>
            )
        })
    }

    const handleOnChange = (e) => {
        console.log(e.target.value)
        changeActiveComic(e.target.value)
    }

    return (
        <div className="ComicsList">
            <h3>ComicsList</h3>
            <p>I agree there are {comics.length} comics</p>
            <select onChange = {handleOnChange}>
                {renderComicOption()}
            </select>
        </div>
      );
}
 
export default ComicsList;