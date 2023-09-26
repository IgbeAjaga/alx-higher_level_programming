#!/usr/bin/node
// Import the request module
const request = require('request');

// Check if the command line arguments include the API URL
if (process.argv.length !== 3) {
  console.error('Usage: node 6-completed_tasks.js <api_url>');
  process.exit(1); // Exit with an error code
}

const apiUrl = process.argv[2]; // Get the API URL from the command line args

// Make a GET request to the specified API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1); // Exit with an error code
  } else {
    // Parse the JSON response to extract task data
    const tasks = JSON.parse(body);

    // Create an object to store the count of completed tasks per user
    const completedTasksByUser = {};

    // Calculate the number of completed tasks for each user
    tasks.forEach((task) => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    // Print the number of completed tasks per user
    console.log(completedTasksByUser);
  }
});
