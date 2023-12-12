#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments

let flag = false;
const arr = process.argv;
let arrNums = [];
if (arr.length < 4) {
  console.log(0);
  flag = true;
} else {
  for (let i = 2; i < arr.length; i++) {
    arrNums.push(Number(arr[i]));
  }
}

if (!flag) {
  const max = Math.max(...arrNums);
  arrNums = arrNums.filter(num => num !== max);
  console.log(Math.max(...arrNums));
}
