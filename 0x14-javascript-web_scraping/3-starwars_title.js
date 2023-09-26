#!/usr/bin/node
// Import the request module
const request = require('request');

// Check if the command line arguments include a movie ID
if (process.argv.length !== 3) {
  console.error('Usage: node 3-starwars_title.js <movie_id>');
  process.exit(1); // Exit with an error code
}

const movieId = process.argv[2]; // Get the movie ID from the commandline
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1); // Exit with an error code
  } else {
    // Parse the JSON response to extract the movie title
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
