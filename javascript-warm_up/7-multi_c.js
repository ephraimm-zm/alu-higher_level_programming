#!/usr/bin/node
const value = parseInt(process.argv[2]);

if (!isNaN(value) && value > 0) {
  for (let x = 0; x < value; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
