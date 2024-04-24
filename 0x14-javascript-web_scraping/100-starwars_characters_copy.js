#!/usr/bin/node
/* a script that prints all characters of a Star Wars movie
 * The first argument is the Movie ID
 */


// const URL = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2]

// const request1 = require("request")
// const request2 = require('request')
// request1(URL, (error, response, body) => {
//   if (error) {
//     console.log(error);
//   } else {
//     if (response && response.statusCode === 200) {
// 		characters = JSON.parse(body).characters;
// 		for (character in characters) {
// 			request2(character, (error, response, body) => {
// 				console.log(JSON.parse(body).name);
// 			});
// 		}
// 	}
//   }
// });

// const request = require('request-promise-native');

async function getCharacters() {
  const URL = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];

  try {
    body = await request (URL);
    const characters = JSON.parse(body);
    for (let character of characters) {
		characterRequest = await request(character);
		console.log(JSON.parse(characterRequest).name);
    }
  } catch (error) {
      console.log(error)
  }
}

getCharacters();
