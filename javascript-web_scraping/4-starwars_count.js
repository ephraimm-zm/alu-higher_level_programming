#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;

    data.characters.forEach(character => {
      if (character.endsWith('18/')) {
        count++;
      }
    });
    console.log(count);
  }
});
