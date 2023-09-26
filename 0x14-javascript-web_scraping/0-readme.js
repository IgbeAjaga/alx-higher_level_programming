#!/usr/bin/node
// Import the fs (file system) module
const fs = require('fs');

// Check if the command line arguments include a file path
if (process.argv.length !== 3) {
  console.error('Usage: node 0-readme.js <file_path>');
  process.exit(1); // Exit with an error code
}

const filePath = process.argv[2]; // Get the file path from the command line arguments

// Read the content of the file in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if an error occurred
    console.error(err);
    process.exit(1); // Exit with an error code
  } else {
    // Print the file content if read successfully
    console.log(data);
  }
});
