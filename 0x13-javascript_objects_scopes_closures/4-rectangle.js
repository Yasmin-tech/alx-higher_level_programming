#!/usr/bin/node
/*
 * a class Rectangle that defines a rectangle:
 * The constructor: take 2 arguments w and h
 * instances: attribute width with the value of w
 *            attribute height with the value of h
 *
 * instance methods: print() -> prints the rectangle using the character X
 *                   rotate() -> exchanges the width and the height of the rectangle
 *                   double() -> multiples the width and the height of the
 *
 * if w or h is equal to 0 or not a positive integer, create an empty object
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const width = this.width;
    this.width = this.height;
    this.height = width;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
