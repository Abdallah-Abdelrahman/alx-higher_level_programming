#!/usr/bin/node
/**
 * Reverse a list
 * @param {Array} list of any type
 * @return {Array} the reversed list
 */
exports.esrever = function (list) {
  let start, end, tmp;

  if (!Array.isArray(list)) return (list);

  start = 0, end = list.length - 1;
  while (start <= end / 2) {
    tmp = list[start];
    list[start] = list[end];
    list[end] = tmp;
    start++;
    end--;
  }
  return (list);
};
