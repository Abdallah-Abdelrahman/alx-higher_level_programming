#!/usr/bin/node
// searches the second biggest integer in the list of arguments
const [, , ...args] = process.argv;

if (!args[0] || !args[1]) console.log(0);
else {
  console.log(args.sort((a, b) => a - b)[args.length - 2]);
}
