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

  if (!Array.isArray(list)) return (list);

  const rev = [...list];
  start = 0;
  end = list.length - 1;
  while (start <= end / 2) {
    tmp = rev[start];
    rev[start] = rev[end];
    rev[end] = tmp;
    start++;
    end--;
  }
  return (rev);
};
