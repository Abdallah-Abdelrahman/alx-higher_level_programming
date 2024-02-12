#!/usr/bin/env node
/** prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
 * If the argument can’t be converted to an integer, print “Not a number”
 */
const { argv } = process;
const n = parseInt(argv[2]);

if (isNaN(n) || isNaN(argv[2])) console.log('Not a number');
else console.log(`My number: ${n}`);
