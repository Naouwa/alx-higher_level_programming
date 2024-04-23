#!/usr/bin/node

// A class Rectangle that defines a rectangle:

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Creating the print instance method
  print () {
    let i = 0;
    for (i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
  }

  // Creating the rotate instance method
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // Creating the double intance method
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
