#!/usr/bin/node
/**
 * @module 101-sorted
 * imports a dictionary of occurrences by user id,
 * and computes a dictionary of user ids by occurrence.
 */
const { dict } = require('./101-data');

const _dict = {};

for (const k in dict) {
  if (!(dict[k] in _dict)) _dict[dict[k]] = [];
  _dict[dict[k]].push(k);
}
console.log(_dict);
