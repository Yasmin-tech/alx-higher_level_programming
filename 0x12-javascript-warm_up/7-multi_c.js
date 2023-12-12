#!/usr/bin/node
const n = process.argv[2];
if (n) {
  let i = 0;
  while (i < n) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
