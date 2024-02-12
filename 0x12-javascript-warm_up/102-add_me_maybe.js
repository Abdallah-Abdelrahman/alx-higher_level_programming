#!/usr/bin/node
/** @module 102-add_me_maybe.js */

/**
 * increments and calls a function.
 * @function
 * @param {number} n
 * @param {function} cb
 */
module.exports.addMeMaybe = function (n, cb) {
  cb(n + 1);
};
