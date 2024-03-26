#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(argv[2], function (_error, response) {
  console.log('code:', response && response.statusCode);
});
