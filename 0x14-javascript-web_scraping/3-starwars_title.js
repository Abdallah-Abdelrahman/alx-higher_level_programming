#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request(url, function (_error, response, body) {
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
