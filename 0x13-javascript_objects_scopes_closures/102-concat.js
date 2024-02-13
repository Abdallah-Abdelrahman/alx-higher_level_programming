#!/usr/bin/node
/**
 * @module 102-concat
 * 1st and 2nd arguments to the program are source files to read from,
 * 3rd argument is the distination file to append the data to
 */
const { readFileSync, appendFileSync } = require('fs');
const { 2: src1, 3: src2, 4: dist } = process.argv;

[src1, src2].forEach(file =>
  appendFileSync(dist, readFileSync(file, 'utf8'))
);
