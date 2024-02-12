#!/usr/bin/node
// script that prints two arguments passed to it, in the following format: “ is ”
const { argv } = process;

console.log(argv[2] + ' is ' + argv[3]);
