#!/usr/bin/node
// a script that writes a string to a file.

const fs = require('fs');
const data = process.argv[3];
const fileName = process.argv[2];

try {
  fs.writeFileSync(fileName, data, 'utf-8');
} catch (error) {
  console.log(error);
}
