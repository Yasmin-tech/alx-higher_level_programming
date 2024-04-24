#!/usr/bin/node
//  a script that reads and prints the content of a file.

const fs = require('fs');
const fileName = './' + process.argv[2];

try {
  const data = fs.readFileSync(fileName, 'utf-8');
  console.log(data);
} catch (error) {
  console.log(error);
}
