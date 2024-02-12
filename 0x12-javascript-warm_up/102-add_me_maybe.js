#!/usr/bin/node
/**
 * @module 102-add_me_maybe.js
 * increments and calls a function.
 * @function
 * @param {number} number
 * @param {function} theFunction
 */
module.exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
