import './SelectedBeer.css'

const SelectedBeer = ({selectedBeer}) => {
    return (
    <div className="SelectedBeer">
        <h3>SelectedBeer</h3>
        {selectedBeer.length === 1 ? <p>Selected Beer not empty</p> : <p>Selected Beer empty</p>}
    </div>  );
}
 
export default SelectedBeer;