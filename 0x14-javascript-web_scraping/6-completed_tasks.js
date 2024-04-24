#!/usr/bin/node

/* a script that computes the number of tasks completed by user id.
 *  API URL: https://jsonplaceholder.typicode.com/todos
 * Only users with completed task are printed
 * Fetch the API resource with request module
 */

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    if (response.statusCode === 200) {
      const responseJSON = JSON.parse(body);
      const result = {};
      let i;
      for (i = 0; i < responseJSON.length; i++) {
        const userId = responseJSON[i].userId;
        if (result[String(userId)] === undefined) {
          result[String(userId)] = 0;
        }
        if (responseJSON[i].completed) {
          result[String(userId)]++;
        }
      }
      console.log(result);
    }
  } else {
    console.log(error);
  }
});
