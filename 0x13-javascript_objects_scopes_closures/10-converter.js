#!/usr/bin/node
/**
 * Converts a number from base 10 to another base passed as argument
 * @param {number} base
 * @return {Function} - callback function that converts from base 10
 */
exports.converter = function (base) {
  return function (number) {
    return (number.toString(base));
  };
};
