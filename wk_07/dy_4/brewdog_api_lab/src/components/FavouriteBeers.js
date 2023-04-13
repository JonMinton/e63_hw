import './FavouriteBeers.css'

import Beer from './Beer';

const FavouriteBeers = ({beers, handleToggleBeerFavourited, handleSelectBeer}) => {

    // Add call to Beer here
    const iterateBeerCalls = () => {
        return beers.map((beer) => {
            return (
                <Beer 
                    key = {beer.id} 
                    name = {beer.name} 
                    handleToggleBeerFavourited = {handleToggleBeerFavourited}
                    handleSelectBeer = {handleSelectBeer}
                />
    
            )
        })
    }

    return (
    <div className="FavouriteBeers">
        <h3>FavouriteBeers</h3>
        <p>There are {beers.length} favourite beers</p>
        {iterateBeerCalls()}
    </div>  );
}
 
export default FavouriteBeers;