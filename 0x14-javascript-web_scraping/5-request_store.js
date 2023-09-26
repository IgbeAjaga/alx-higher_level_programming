#!/usr/bin/node
// Import the request module
const request = require('request');
const fs = require('fs');

// Check if the command line arguments include a URL and a file path
if (process.argv.length !== 4) {
  console.error('Usage: node 5-request_store.js <URL> <file_path>');
  process.exit(1); // Exit with an error code
}

const url = process.argv[2]; // Get the URL from the command line arguments
const filePath = process.argv[3]; // Get the file path from the command line

// Make a GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1); // Exit with an error code
  } else {
    // Write the response body to the specified file in utf-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
        process.exit(1); // Exit with an error code
      } else {
        console.log(`Webpage content saved to ${filePath}`);
      }
    });
  }
});
