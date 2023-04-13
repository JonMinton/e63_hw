import './Beer.css'

const Beer = ({name}) => {
    return (
    <div className="Beer">
        <p>This beer is called {name}</p>
    </div>  );
}
 
export default Beer;
