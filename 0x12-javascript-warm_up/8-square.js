#!/usr/bin/node
/**
 * prints a square.
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer, print “Missing size”
 */
const [, , arg] = process.argv;
const n = parseInt(arg);
let s = '';

if (isNaN(n)) console.log('Missing size');
else if (n >= 0) {
  for (let i = 0; i < n; i++, s += i < n ? '\n' : '') {
    for (let j = 0; j < n; j++) {
      s += 'X';
    }
  }
  console.log(s);
}
