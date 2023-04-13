import Beer from "./Beer";

import './AllBeers.css';

const AllBeers = ({beers, handleToggleBeerFavourited, handleSelectBeer}) => {

    const iterateBeerCalls = () => {
        return beers.map((beer) => {
            return (
                <Beer 
                    key = {beer.id} 
                    id = {beer.id}
                    name = {beer.name} 
                    favourite = {beer.favourite}
                    handleToggleBeerFavourited = {handleToggleBeerFavourited}
                    handleSelectBeer = {handleSelectBeer}
                />
    
            )
        })
    }

    return (
    <div className="AllBeers">
        <h3>AllBeers</h3>
        <p>There are {beers.length} beers</p>
        {iterateBeerCalls()}
    </div>
    
    );
}
 
export default AllBeers;