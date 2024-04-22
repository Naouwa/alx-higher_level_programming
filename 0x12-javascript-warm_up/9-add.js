#!/usr/bin/node

// A script that prints the addition of 2 integers

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
