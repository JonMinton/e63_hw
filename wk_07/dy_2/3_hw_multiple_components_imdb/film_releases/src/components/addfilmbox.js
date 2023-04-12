import React, { useState } from 'react';


const AddFilmBox = ({onFilmSubmit}) => {

    const [name, setName] = useState("");
    const [url, setUrl] = useState("");

    const handleNameChange = e => setName(e.target.value)
    const handleUrlChange = e => setUrl(e.target.value)
    const handleSubmit = e => {
        e.preventDefault();
        const nameValue = name.trim()
        const urlValue = url.trim()
        if (!nameValue || !urlValue) return // Return and do nothing if no valid input
        // Update comments in CommentBox
        onFilmSubmit({
            name: nameValue,
            url: urlValue
        })
        // Clear the inputs
        setName('')
        setUrl('')

    }


    return (
        <form onSubmit = {handleSubmit}> 
            <input type = "name" placeholder = "Film name" value = {name} onChange = {handleNameChange}/>
            <input type = "url" placeholder = "Film URL" value = {url} onChange = {handleUrlChange}/>
            <button>Submit</button>
        </form>
      );



}
 
export default AddFilmBox;