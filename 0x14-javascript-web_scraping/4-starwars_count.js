#!/usr/bin/node
// Import the request module
const request = require('request');

// Check if the command line arguments include the API URL
if (process.argv.length !== 3) {
  console.error('Usage: node 4-starwars_count.js <api_url>');
  process.exit(1); // Exit with an error code
}

const apiUrl = process.argv[2]; // Get the API URL from the command line args

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1); // Exit with an error code
  } else {
    // Parse the JSON response to extract movie data
    const movieData = JSON.parse(body);

    // Filter the movies where "Wedge Antilles" (character ID 18) is present
    const moviesWithWedgeAntilles = movieData.results.filter((movie) =>
      movie.characters.includes(
	      'https://swapi-api.alx-tools.com/api/people/18/')
    );

    // Print the number of movies with "Wedge Antilles"
    console.log(moviesWithWedgeAntilles.length);
  }
});
