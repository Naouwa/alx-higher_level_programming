#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// The URL to request is provided as the first argument
const url = process.argv[2];
// The file path to store the body response is provided as the second argument
const filePath = process.argv[3];

// Make a GET request to fetch the contents of the webpage
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(filePath, body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
