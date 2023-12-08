#!/usr/bin/node
const axios = require('axios');

function getMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  return axios.get(url)
    .then(response => {
      const charactersUrls = response.data.characters;
      const promises = charactersUrls.map(charUrl => axios.get(charUrl));

      return Promise.all(promises)
        .then(charactersData => {
          const charactersNames = charactersData.map(charData => charData.data.name);
          return charactersNames;
        })
        .catch(error => {
          console.error('Error fetching characters:', error);
          return null;
        });
    })
    .catch(error => {
      console.error('Error fetching movie data:', error);
      return null;
    });
}

function printCharacterNames(movieId) {
  getMovieCharacters(movieId)
    .then(characters => {
      if (characters) {
        characters.forEach(character => {
          console.log(character);
        });
      } else {
        console.log('Error fetching characters. Please check the Movie ID.');
      }
    });
}
