#!/usr/bin/node
const OldSquare = require('./5-square');

/**
 * Class reperesents Square.
 * @extends Rectangle
 */
module.exports = class Square extends OldSquare {
  /**
   * Print a square
   * @param {string=} c
   */
  charPrint (c) {
    let s = '';
    if (this.width && this.height) {
      s =
        [...Array(this.height)]
          .map(_ => [...Array(this.width)].map(_ => c || 'X').join(''))
          .join('\n');
    }
    console.log(s);
  }
};
