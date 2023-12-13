#!/usr/bin/node
/*
 * a class Square that defines a square and inherits from Square of 5-square.js
 * instance method: charPrint(c) -> prints the using the character c, If c is undefined, use the character X
 *
 */

const SuperSquare = require('./5-square.js');
class Square extends SuperSquare {
  charPrint (c) {
    let character = c;
    if (character === undefined) {
      character = 'x';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(character.repeat(this.width));
    }
  }
}
module.exports = Square;
