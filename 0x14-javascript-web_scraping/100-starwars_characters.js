#!/usr/bin/node
/* a script that prints all characters of a Star Wars movie
 * The first argument is the Movie ID
 */

const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(URL, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  } else {
    console.log(error);
  }
});

function printCharacters (characters, i) {
  if (i < characters.length) {
    request(characters[i], (error, response, body) => {
      if (!error && response.statusCode === 200) {
        console.log(JSON.parse(body).name);
        printCharacters(characters, i + 1); // Recursive call to the next character
      } else {
        console.log(error);
      }
    });
  }
}
