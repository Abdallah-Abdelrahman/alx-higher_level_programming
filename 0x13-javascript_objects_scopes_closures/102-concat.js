#!/usr/bin/node
const { readFileSync, appendFileSync } = require('fs');
const { 2: src1, 3: src2, 4: dist } = process.argv;

[src1, src2].forEach(file =>
  appendFileSync(dist, readFileSync(file, 'utf8'))
);
