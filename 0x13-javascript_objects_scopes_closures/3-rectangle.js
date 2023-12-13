#!/usr/bin/node
/*
 * a class Rectangle that defines a rectangle:
 * The constructor: take 2 arguments w and h
 * instances: attribute width with the value of w
 *            attribute height with the value of h
 *
 * methods: print() -> prints the rectangle using the character X
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
}
module.exports = Rectangle;
