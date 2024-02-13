#!/usr/bin/node
/**
 * Reverse a list
 * @param {Array} list of any type
 * @return {Array} the reversed list
 */
exports.esrever = function (list) {
  let start;
  let end;
  let tmp;
  let rev = null;

  if (!Array.isArray(list)) return (list);

  rev = [...list];
  start = 0;
  end = list.length - 1;
  while (start < end) {
    tmp = rev[start];
    rev[start] = rev[end];
    rev[end] = tmp;
    start++;
    end--;
  }
  return (rev);
};
