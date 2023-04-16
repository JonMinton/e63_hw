const YearSelect = ({years, handleYearFilter}) => {


    const selectionOfYears = () => {
        return (
            years.map(year => {
                return (
                    <option key = {year} value = {year}>{year}</option>
                )
            })
        )
    }

    const handleOnChange = (e) => {
        console.log(e.target.value)
        handleYearFilter(e.target.value)
    }

    return (
        <div>
            <h4>YearSelect</h4>  
            <select onChange = {handleOnChange}>
                <option key = {0} value = {""}>All Years</option>
                {selectionOfYears()}
            </select>
        </div>
    );
}
 
export default YearSelect;