#!/usr/bin/node
const request = require('request');
const { argv } = process;
const api = 'https://swapi-api.alx-tools.com/api';

request(`${api}/films/${argv[2]}`, async function (_error, response, body) {
  const characters = [];
  if (response.statusCode === 200) {
    characters.push(...JSON.parse(body).characters);
    for await (const name of charactersGenerator(characters)) {
      console.log(name);
    }
  }
});

async function * charactersGenerator (chars) {
  for (const ch of chars) {
    yield new Promise((resolve, reject) => {
      request(ch, function (error, response, body) {
        if (error) { reject(error); }
        if (response.statusCode === 200) {
          resolve(JSON.parse(body).name);
        }
      });
    });
  }
}
