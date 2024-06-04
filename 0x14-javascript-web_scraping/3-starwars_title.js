#!/usr/bin/node

const request = require('request');

// The base URL for the Star Wars API
const baseUrl = 'https://swapi-api.alx-tools.com/api/films';

// The movie ID is provided as the first argument
const movieId = process.argv[2];

// Make a GET request to fetch information about the specified movie ID
request(`${baseUrl}/${movieId}`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body as JSON
  const movieInfo = JSON.parse(body);

  // Print the title of the movie
  console.log(movieInfo.title);
});
