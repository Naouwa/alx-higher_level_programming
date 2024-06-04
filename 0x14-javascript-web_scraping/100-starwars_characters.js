#!/usr/bin/node

const request = require('request');

// The movie ID is provided as the first argument
const movieId = process.argv[2];

// Construct the URL for fetching movie information
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to fetch information about the movie
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body as JSON
  const movie = JSON.parse(body);

  // Fetch characters for the movie
  const promises = movie.characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (err, res, body) => {
        if (err) {
          reject(err);
          return;
        }

        // Parse the character details as JSON
        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  });

  // Resolve all promises and print character names
  Promise.all(promises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(err => console.error(err));
});
