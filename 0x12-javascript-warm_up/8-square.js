#!/usr/bin/node

let xSize = parseInt(process.argv[2]);
if (isNaN(xSize) || process.argv ===  undefined) {
  console.log('Missing size');
}

myVar = 'X';
for (let i = 0; i < xSize - 1; i++) {
  myVar += 'X';
}
while (xSize > 0) {
  console.log(myVar);
  xSize--;
}
