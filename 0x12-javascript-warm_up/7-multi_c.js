#!/usr/bin/node

let xPrint = parseInt(process.argv[2]);
if (isNaN(xPrint) || process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  while (xPrint > 0) {
    console.log('C is fun');
    xPrint--;
  }
}
