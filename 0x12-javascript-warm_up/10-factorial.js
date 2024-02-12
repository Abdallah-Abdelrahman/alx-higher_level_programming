#!/usr/bin/node
/** @module 10-factorial.js */

const [, , arg] = process.argv;
const n = parseInt(arg);

if (isNaN(n)) console.log(1);
else console.log(factorial(n));

/**
 * computes factorial
 * @param {number} x
 *
 * @return {number} factorial @x
 */
function factorial (x) {
  if (x < 2) return (1);

  return (x * factorial(x - 1));
}
