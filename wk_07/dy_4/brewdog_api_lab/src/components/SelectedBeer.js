import './SelectedBeer.css'

const SelectedBeer = ({selectedBeer}) => {
    console.log("SelectedBeer triggered")
    console.log(selectedBeer)
    selectedBeer === null ? console.log("SB UNDEFINED") : console.log("SB NOT UNDEFINED")
    // console.log(`The selected beer is ${selectedBeer.name}`)
    return (
    <div className="SelectedBeer">
        <h3>SelectedBeer</h3>
        {selectedBeer === null ?
          null : 
         <p>The selected beer is {selectedBeer.name}</p>
        }
    </div>  );
}
 
export default SelectedBeer;