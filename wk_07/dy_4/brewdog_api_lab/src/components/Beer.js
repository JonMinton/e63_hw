import './Beer.css'

const Beer = ({id, name, favourite, handleToggleBeerFavourited, handleSelectBeer}) => {

    console.log(`id: ${id}; favourite: ${favourite}`)

    const handleMakeFavourite = () => {
        console.log("handleMakeFavourite triggered")
        handleToggleBeerFavourited(id)
    }

    const handleMakeUnfavourite = () => {
        console.log("handleMakeUnfavourite triggered")
        handleToggleBeerFavourited(id)

    }


    return (
    <div className="Beer">
        <span>
            This beer is called {name}
                {
                    favourite ? 
                    <span onClick = {handleMakeUnfavourite} className="Make-Beer-Unfavourite">   UNFAVOURITE   </span> : 
                    <span onClick = {handleMakeFavourite} className="Make-Beer-favourite">   FAVOURITE   </span>
                }
        </span>
    </div>  );
}
 
export default Beer;
