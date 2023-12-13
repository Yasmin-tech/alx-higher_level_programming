#!/usr/bin/node
// a function that returns the reversed version of a list:

exports.esrever = function (list) {
  const reversedList = [];
  const size = list.length;

  for (let i = size - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return (reversedList);
};
