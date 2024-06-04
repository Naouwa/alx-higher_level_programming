#!/usr/bin/node

const request = require('request');

// The API URL is provided as the first argument
const apiUrl = process.argv[2];

// Wedge Antilles character ID
const WEDGE_ANTILLES_ID = 18;

// Make a GET request to fetch information about Star Wars films
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body as JSON
  const filmsData = JSON.parse(body);

  // Initialize a variable to count films with Wedge Antilles
  let filmsWithWedgeAntillesCount = 0;

  // Iterate through each film
  filmsData.results.forEach(film => {
    // Check if Wedge Antilles is among the characters in the current film
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${WEDGE_ANTILLES_ID}/`)) {
    // Increment the count if Wedge Antilles is present in the film
      filmsWithWedgeAntillesCount++;
    }
  });

  // Print the number of films with Wedge Antilles
  console.log(filmsWithWedgeAntillesCount);
});
