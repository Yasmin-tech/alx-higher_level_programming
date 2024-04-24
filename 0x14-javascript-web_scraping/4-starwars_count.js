#!/usr/bin/node
/* a script that prints the number of movies where the character “Wedge Antilles” is present
 * Star wars API: https://swapi-api.alx-tools.com/api/films/
 * Wedge Antilles is character ID 18
 * With the module request
 */

const request = require('request');
let counter = 0;
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const responseJSON = JSON.parse(body);
    const results = responseJSON.results;
    let i;
    let j;
    for (i = 0; i < results.length; i++) {
      const listCharacter = results[i].characters;
      for (j = 0; j < listCharacter.length; j++) {
        if (listCharacter[j].includes('18')) {
          counter += 1;
        }
      }
    }
  }
  console.log(counter);
});
