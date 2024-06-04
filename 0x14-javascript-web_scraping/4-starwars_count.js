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

  // Filter films where Wedge Antilles is present
  const filmsWithWedgeAntilles = filmsData.results.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${WEDGE_ANTILLES_ID}/`)
  );

  // Print the number of films with Wedge Antilles
  console.log(filmsWithWedgeAntilles.length);
});
