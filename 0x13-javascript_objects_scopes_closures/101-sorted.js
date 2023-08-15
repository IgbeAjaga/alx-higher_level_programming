#!/usr/bin/node
const dict = require('./101-data').dict;

const sortedDict = {};
for (const key in dict) {
  if (dict[key] in sortedDict) {
    sortedDict[dict[key]].push(key);
  } else {
    sortedDict[dict[key]] = [key];
  }
}

console.log(sortedDict);
