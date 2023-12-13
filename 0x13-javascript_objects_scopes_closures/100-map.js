#!/usr/bin/node
// a script that imports an array and computes a new array

const list1 = require('./100-data.js').list;
let index = 0;
const list2 = list1.map((x) => x * index++);
console.log(list1);
console.log(list2);
