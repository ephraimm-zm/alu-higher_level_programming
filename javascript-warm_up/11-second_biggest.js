#!/usr/bin/node
const argv = process.argv.slice(2);

if (argv.length === 0) {
  console.log('0');
  process.exit();
}

if (argv.length === 1) {
  console.log('1');
  process.exit();
}

let highest = Number(argv[0]);
let second = Number.NEGATIVE_INFINITY;

for (let i = 1; i < argv.length; i++) {
  const num = Number(argv[i]);

  if (num > highest) {
    second = highest;
    highest = num;
  } else if (num > second && num < highest) {
    second = num;
  }
}

console.log(second);
