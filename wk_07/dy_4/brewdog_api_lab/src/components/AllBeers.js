import Beer from "./Beer";

import './AllBeers.css';

const AllBeers = ({beers}) => {

    const iterateBeerCalls = () => {
        return beers.map((beer) => {
            return <Beer key = {beer.id} name = {beer.name} />
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