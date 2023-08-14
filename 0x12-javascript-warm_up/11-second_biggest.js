#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);
  const max = Math.max(...args);
  args.splice(args.indexOf(max), 1);
  console.log(Math.max(...args));
}
