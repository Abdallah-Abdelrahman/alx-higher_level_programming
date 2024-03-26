#!/usr/bin/node
const request = require('request');
const argv = process.argv;

if (argv[2]) {
  request(argv[2], function (error, response, body) {
    if (error) { return console.log(error); }

    if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      let count = 0;
      for (const { characters } of films) {
        if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          count++;
        }
      }
      console.log(count);
    }
  });
}
