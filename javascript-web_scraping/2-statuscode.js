#!/usr/bin/node

const request = require('request');
const urlPath = process.argv[2];

request.get(urlPath, (error, response, body) => {
if (error) {
console.error(error);
} else {
console.log("code: " + response.statusCode);
}
});
