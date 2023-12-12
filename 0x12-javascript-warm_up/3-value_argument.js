#!/usr/bin/nodejs
if (process.argv[2]) {
  console.log(process.argv[2]);
  console.log(process.argv[2].length);
} else {
  console.log('No argument');
}
