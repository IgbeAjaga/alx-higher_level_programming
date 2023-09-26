#!/usr/bin/node
const filepth = require('filepth');
filepth.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
