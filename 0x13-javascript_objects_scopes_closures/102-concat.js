#!/usr/bin/node
const { readFile, appendFile } = require('node:fs');
const { 2: src1, 3: src2, 4: dist } = process.argv;

[src1, src2].forEach(file => {
  readFile(file, 'utf8', (err, data) => !err && appendFile(dist, data));
});
