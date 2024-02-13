#!/usr/bin/node
/**
 * returns the number of occurrences in a list.
 * @param {Array.<number>} list
 * @param {number} searchElement
 * @return {number} number of occurrences
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  if (!list || !Array.isArray(list)) return (0);
  for (const el of list) {
    if (el === searchElement) count++;
  }
  return (count);
};
