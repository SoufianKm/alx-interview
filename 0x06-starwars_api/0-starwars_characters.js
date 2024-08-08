#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');


/**
 * Wrapper function for request object that allows it
 * to work with async and await.
 * @param   {String} url - site url
 * @returns {Promise}    - promise object that resolves
 *                         with parsed JSON response
 *                         and rejects with the request error.
 */
function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}


/**
 * Entry point - makes requests to Star Wars API
 * for movie info based on the movie ID passed as a CLI parameter.
 * Retrieves movie character info then prints their names
 * in order of appearance in the initial response.
 */
async function main () {
  const args = process.argv;

  // Ensure a movie ID is provided as a command-line argument
  if (args.length < 3) {
    return;
  }

  // Construct the movie URL using the provided movie ID
  const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];

  try {
    // Fetch the movie details
    const movie = await makeRequest(movieUrl);

    // Ensure the movie has characters
    if (!movie.characters) {
      return;
    }

    // Fetch and print each character's name
    for (const characterUrl of movie.characters) {
      const character = await makeRequest(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

// Run the main function
main();
