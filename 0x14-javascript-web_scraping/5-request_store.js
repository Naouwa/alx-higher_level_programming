#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// The URL to request is provided as the first argument
const url = process.argv[2];
// The file path to store the body response is provided as the second argument
const filePath = process.argv[3];

// Make a GET request to fetch the contents of the webpage
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Write the body response to the specified file path
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(`File saved to ${filePath}`);
  });
});
