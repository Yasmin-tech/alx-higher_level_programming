#!/usr/bin/node
// a function that returns the number of occurrences in a list:

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const element of list) { // for...in -> key/index for...let..of -> get the value
    if (element === searchElement) {
      counter++;
    }
  }
  return (counter);
};
