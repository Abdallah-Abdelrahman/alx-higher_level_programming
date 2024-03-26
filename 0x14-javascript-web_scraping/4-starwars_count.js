#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(argv[2], function (_error, response, body) {
  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const number = films.reduce((acc, { characters }) => {
      return characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
        ? acc + 1
        : acc;
    }, 0);
    console.log(number);
  }
});
