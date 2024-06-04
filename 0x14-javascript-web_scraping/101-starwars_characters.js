#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  if (index < characters.length) {
    request(characters[index], function (error, response, body) {
      if (!error) {
        console.log(JSON.parse(body).name);
        printCharacters(characters, index + 1);
      }
    });
  }
}
