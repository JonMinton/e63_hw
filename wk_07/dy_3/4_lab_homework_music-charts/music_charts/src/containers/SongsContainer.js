import React, { useState, useEffect } from 'react';

import SongList from '../components/SongList';
import GenreSelect from '../components/GenreSelect';

const SongsContainer = ({songs}) => {

    return (
        <>
            <h2>I'm a big box of songs</h2>
            <GenreSelect />
            {songs ? <SongList songs = {songs} /> : null}
        </>

      );
}
 
export default SongsContainer;