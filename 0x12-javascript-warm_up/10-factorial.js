#!/usr/bin/node
// A function that computes and prints a factorial

function factorial (num) {
  if (isNaN(num) || num === 1) {
    return 1;
  }

  return num * factorial(num - 1);
}

const num = Number(process.argv[2]);
console.log(factorial(num));
