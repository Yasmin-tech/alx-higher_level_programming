#!/usr/bin/nodejs
const argc = process.argv;
if (argc[2]) {
  console.log(argc[2]);
} else {
  console.log('No argument');
}
