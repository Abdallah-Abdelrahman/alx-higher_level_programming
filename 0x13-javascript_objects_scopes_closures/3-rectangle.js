#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let s = '';
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++, s += i < this.height ? '\n' : '') {
        for (let j = 0; j < this.width; j++) {
          s += 'X';
        }
      }
    }
    console.log(s);
  }
};
