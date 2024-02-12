#!/usr/bin/node
/**
 * @module 103-object_fct.js
 * add new function incr that increments the integer value.
 */
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () {
  this.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
