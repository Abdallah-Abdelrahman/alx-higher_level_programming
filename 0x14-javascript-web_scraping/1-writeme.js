#!/usr/bin/node
const { writeFile } = require('fs');
const argv = process.argv;

writeFile(argv[2], argv[3], 'utf8', (err) => {
  if (err) { console.log(err); }
});
