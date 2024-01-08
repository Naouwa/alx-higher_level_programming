#!/usr/bin/node

// Ascript that prints a square

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);
  for (let row = 0; row < size; row++) {
    console.log('X'.repeat(size));
  }
}
