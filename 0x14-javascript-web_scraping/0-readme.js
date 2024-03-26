#!/usr/bin/node
const { readFile } = require('fs');
const argv = process.argv;

readFile(argv[2], 'utf8', (err, data) => {
  if (err) { console.log(err); } else { console.log(data); }
});
