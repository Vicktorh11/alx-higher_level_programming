#!/usr/bin/node

function factorial (n) {
  if (n <= 0) {
    return 0;
  } else if (n === 1) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}

const myInt = parseInt(process.argv[2]);
if (isNaN(myInt)) {
  console.log('1');
} else {
  console.log(factorial(myInt));
}


