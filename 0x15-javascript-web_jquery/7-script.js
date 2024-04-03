// Waits for the document to be ready
$(document).ready(function () {
  // Fetches the character data from the URL
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Extracts the character name from the fetched data
    const characterName = data.name;
    // This displays the character name in the DIV#character
    $('DIV#character').text(characterName);
  });
});
