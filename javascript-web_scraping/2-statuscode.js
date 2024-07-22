#!/usr/bin/node
const request = require('request');
const urlPath = process.argv[2];

request(urlPath, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
