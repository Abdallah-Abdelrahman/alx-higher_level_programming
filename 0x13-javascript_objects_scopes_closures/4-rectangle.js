#!/usr/bin/node
/** Class represents Rectangle */
module.exports = class Rectangle {
  /**
   * Create a Rectangle
   * @param {number} w - width
   * @param {number} h - height
   */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /** Print a Rectangle */
  print () {
    let s = '';
    if (this.width && this.height) {
      s =
        [...Array(this.height)]
          .map(_ => [...Array(this.width)].map(_ => 'X').join(''))
          .join('\n');
    }
    console.log(s);
  }

  /** Exchange width and height of the Rectangle */
  rotate () {
    this.width ^= this.height;
    this.height ^= this.width;
    this.width ^= this.height;
  }

  /** Multiply width and height by 2 */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
