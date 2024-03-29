#!/usr/bin/node

/* a class named Sqaure */
const Square1 = require('./5-square');

class Square extends Square1 {
	charPrint(c) {
		if (c === undefined) {
			this.print();
		} else {
			for (let i = 0; i < this.height; i++) {
				console.log(c.repeat(this.width));
			}
		}
	}
}
module.exports = Square;
