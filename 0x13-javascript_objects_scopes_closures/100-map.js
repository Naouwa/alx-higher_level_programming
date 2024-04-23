#!/usr/bin/node

// A script that imports an array and computes a new array.

const list = require('./100-data.js').list;

const comList = list.map((item, index) => item * index);

console.log(list);
console.log(comList);
