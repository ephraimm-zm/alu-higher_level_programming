#!/usr/bin/node
const requests = require('requests');

const targetURL = process.argv[2];

requests.get(targetURL, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const todos = JSON.parse(body);
  const users = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (users[todo.userId]) {
        users[todo.userId]++;
      } else {
        users[todo.userId] = 1;
      }
    }
  });
  console.log(users);
});
