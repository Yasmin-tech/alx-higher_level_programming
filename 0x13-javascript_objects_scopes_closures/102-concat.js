#!/usr/bin/node
const fs = require('fs');

fs.readFile('./fileA', function (err, data) {
  if (err) throw err;
  const f1 = data.toString();

  fs.readFile('./fileB', function (err, data) {
    if (err) throw err;
    const f2 = data.toString();

    fs.writeFile('./fileC', f1 + f2, function (err) {
      if (err) throw err;
    });
  });
});
