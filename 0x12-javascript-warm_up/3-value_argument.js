#!/usr/bin/node
// prints the first argument passed to it:
const { argv } = process;

if (!argv[2]) console.log('No argument');
else console.log(argv[2]);
