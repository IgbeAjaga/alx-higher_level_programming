#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];

const content1 = fs.readFileSync(file1Path, 'utf-8');
const content2 = fs.readFileSync(file2Path, 'utf-8');
const concatenatedContent = content1 + content2;

fs.writeFileSync(destinationPath, concatenatedContent);
