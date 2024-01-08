#!/usr/bin/node

// A script that prints a message depending of the number of arguments passed

if (process.argv.length === 2) {
  console.log('No agument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
