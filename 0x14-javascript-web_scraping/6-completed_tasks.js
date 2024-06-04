#!/usr/bin/node

const request = require('request');

// The API URL is provided as the first argument
const apiUrl = process.argv[2];

// Make a GET request to fetch information about tasks
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body as JSON
  const tasksData = JSON.parse(body);

  // Aggregate the number of completed tasks by user id
  const completedTasksByUser = tasksData.reduce((acc, task) => {
    if (task.completed) {
      acc[task.userId] = (acc[task.userId] || 0) + 1;
    }
    return acc;
  }, {});

  // Print the aggregate count of completed tasks by user id
  console.log(completedTasksByUser);
});
