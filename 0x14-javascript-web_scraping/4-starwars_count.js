#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(argv[2], function (error, response, body) {
  if (error) { return console.log(error); }
  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const number = films.reduce((acc, { characters }) => {
      if (characters.indexOf('https://swapi-api.alx-tools.com/api/people/18/') >= 0) {
        acc++;
      }
      return acc;
    }, 0);
    console.log(number);
  }
});
