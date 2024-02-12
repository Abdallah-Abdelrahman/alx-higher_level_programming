#!/usr/bin/node

const [, , arg1, arg2] = process.argv;

console.log(add(parseInt(arg1), parseInt(arg2)));

/**
 * sums 2 integers.
 * @param {number} a - first argument is the first integer
 * @param {number} b - second argument is the second intege
 *
 * @return {number} the sum of @a and @b
 */
function add (a, b) {
  return (a + b);
}
