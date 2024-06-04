#!/usr/bin/node

const request = require('request');

// The API URL is provided as the first argument
const URL = process.argv[2];

// Make a GET request to fetch information about Star Wars films
request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (body) {
    // Wedge Antilles is character ID 18 - use this ID for filtering the
    const json = JSON.parse(body);
    const filmsChars = json.results.filter(
      x => x.characters.find(y => y.match(/\/people\/18\/?$/))
    );
    // Print the number of films with Wedge Antilles
    console.log(filmsChars.length);
  }
});
