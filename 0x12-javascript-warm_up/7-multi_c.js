#!/usr/bin/node
// prints x times “C is fun”
const { argv } = process;
const n = parseInt(argv[2]);

if (isNaN(n)) console.log('Missing number of occurrences');
else if (n >= 0) [...Array(n)].forEach(_ => console.log('C is fun'));
