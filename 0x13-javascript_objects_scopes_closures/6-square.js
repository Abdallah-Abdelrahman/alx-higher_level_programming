#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/**
 * Class reperesents Square.
 * @extends Rectangle
 */
module.exports = class Square extends Rectangle {
  /**
   * Create a Square
   * @param {number} size
   */
  constructor (size) {
    super(size, size);
  }

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
