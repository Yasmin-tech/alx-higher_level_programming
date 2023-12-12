#!/usr/bin/node
// a function that prints the sum of the two command-line arguments

function add (a, b) {
  return a + b;
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
console.log(add(a, b));
