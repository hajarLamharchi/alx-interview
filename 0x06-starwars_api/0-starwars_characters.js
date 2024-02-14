#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const options = { json: true };
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieID;

request(url, options, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  for (const character of body.characters) {
    request(character, options, (error, response, body) => {
      if (error) {
        console.error(error);
      }

      console.log(body.name);
    });
  }
});
