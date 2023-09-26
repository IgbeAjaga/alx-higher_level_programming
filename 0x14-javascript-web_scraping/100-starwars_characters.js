#!/usr/bin/node
// Import the request module
const request = require('request');

// Check if the command line arguments include the movie ID
if (process.argv.length !== 3) {
  console.error('Usage: node 100-starwars_characters.js <movie_id>');
  process.exit(1); // Exit with an error code
}

const movieId = process.argv[2]; // Get the movie ID from the command line
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1); // Exit with an error code
  } else {
    // Parse the JSON response to extract movie data
    const movieData = JSON.parse(body);

    // Print the names of all characters in the movie
    movieData.characters.forEach((characterUrl) => {
      // Make a GET request to the character's URL to get the character's name
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  }
});
