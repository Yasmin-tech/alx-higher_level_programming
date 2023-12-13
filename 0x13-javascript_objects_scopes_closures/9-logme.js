#!/usr/bin/node
/* a function that prints the number of arguments already printed and the new argument value.
 * logMe("Hello");
 * logMe("Best");
 * logMe("School");
 * the result:
 * 0: Hello
 * 1: Best
 * 2: School
 */

exports.logMe = function (item) {
  if (this.counter === undefined) {
    this.counter = 0;
  } else {
    this.counter++;
  }
  console.log(`${this.counter}: ${item}`);
};
