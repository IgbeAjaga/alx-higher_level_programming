#!/usr/bin/node
// Import the fs (file system) module
const fs = require('fs');

// Check if the command line args include a file path and a string to write
if (process.argv.length !== 4) {
  console.error('Usage: node 1-writeme.js <file_path> <string_to_write>');
  process.exit(1); // Exit with an error code
}

const filePath = process.argv[2]; // Get the file path from command line arg
const stringToWrite = process.argv[3]; // Get string to write from comndln arg

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error occurred
    console.error(err);
    process.exit(1); // Exit with an error code
  } else {
    console.log(`The string "${stringToWrite}" has been written to ${filePath}`);
  }
});
