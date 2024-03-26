#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(argv[2], function (_error, response, body) {
  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    console.log(todos.reduce((acc, t) => {
      if (t.completed) {
        acc[t.userId] = t.userId in acc ? acc[t.userId] + 1 : 1;
      }
      return acc;
    }, {}));
  }
});
