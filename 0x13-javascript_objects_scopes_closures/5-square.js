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
};
