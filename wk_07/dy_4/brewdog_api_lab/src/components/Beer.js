import './Beer.css'

const Beer = ({id, name, favourite, handleToggleBeerFavourited, handleSelectBeer}) => {


    const handleMakeFavourite = () => {
        console.log("handleMakeFavourite triggered")
        handleToggleBeerFavourited(id)
    }

    const handleMakeUnfavourite = () => {
        console.log("handleMakeUnfavourite triggered")
        handleToggleBeerFavourited(id)

    }

    const handleBeerSelected = () => {
        console.log("handleBeer triggered")
        handleSelectBeer(id)
    }

    const showFavouriteStatus = () => {
        if (handleToggleBeerFavourited !== null) {
            return (
                favourite ? 
                <span onClick = {handleMakeUnfavourite} className="Make-Beer-Unfavourite">   UNFAVOURITE   </span> : 
                <span onClick = {handleMakeFavourite} className="Make-Beer-favourite">   FAVOURITE   </span>
            )
        } 
    }

    return (
    <div className="Beer">
        <span>
            <span onClick = {handleBeerSelected}>This beer is called {name}</span>
                {showFavouriteStatus()}

        </span>
    </div>  );
}
 
export default Beer;
