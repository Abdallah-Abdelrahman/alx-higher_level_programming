#!/usr/bin/node
const request = require('request');
const { writeFile } = require('fs');
const argv = process.argv;

request(argv[2], function (_error, response, body) {
  if (response.statusCode === 200) {
    writeFile(argv[3], body, 'utf8', (err) => err && console.log(err));
  }
});
