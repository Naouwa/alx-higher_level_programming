#!/usr/bin/node

// A script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const dict = require('./101-data').dict;
const newDict = {};

for (const k in dict) {
  const occurences = dict[k];
  newDict[occurences] = [];
  for (const k in dict) {
    if (dict[k] === occurences) {
      newDict[occurences].push(k);
    }
  }
}
console.log(newDict);
