#!/usr/bin/node
/* a script that prints the title of a Star Wars movie where the episode number matches a given integer
 * The first argument is the movie ID
 * Using Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
 * With the module request
 */

const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  }
});
