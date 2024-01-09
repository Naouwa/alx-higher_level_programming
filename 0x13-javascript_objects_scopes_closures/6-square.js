#!/usr/bin/node

// A class Square that defines a square and inherits from Square of 5-square.js:

const Rectangle = require('./5-square.js');
class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i = 0;
      for (i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
