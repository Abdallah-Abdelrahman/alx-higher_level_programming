#!/usr/bin/node
/** @module 101-call_me_moby */

/**
 * executes x times a function.
 * @param {number} x
 * @param {function} cb
 */
function callMeMoby (x, cb) {
  for (let i = 0; i < x; i++) {
    cb();
  }
}

exports.callMeMoby = callMeMoby;
