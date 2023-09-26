#!/usr/bin/node
// Import the request module
const request = require('request');

// Check if the command line arguments include a URL
if (process.argv.length !== 3) {
  console.error('Usage: node 2-statuscode.js <URL>');
  process.exit(1); // Exit with an error code
}

const url = process.argv[2]; // Get the URL from the command line arguments

// Make a GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1); // Exit with an error code
  } else {
    // Display the status code of the response
    console.log(`code: ${response.statusCode}`);
  }
});
