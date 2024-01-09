#!/usr/bin/node

// A class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
    // Returns an empty object if conditions are met
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
