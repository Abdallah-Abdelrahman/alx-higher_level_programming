#!/usr/bin/node

const [, , arg1, arg2] = process.argv;

console.log(add(parseInt(arg1), parseInt(arg2)));

/**
 * add - sums 2 integers.
 * @a: first argument is the first integer
 * @b: second argument is the second intege
 *
 * Return: the sum of @a and @b
 */
function add (a, b) {
  return (a + b);
}
