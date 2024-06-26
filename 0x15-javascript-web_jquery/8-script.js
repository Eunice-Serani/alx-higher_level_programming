// Waits for the document to be ready
$(document).ready(function () {
  // Fetches the movies data from the URL
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // This iterates through each movie in the fetched data
    $.each(data.results, function (index, movie) {
      // Extracts the movie title
      const title = movie.title;
      // Creates a new list item with the movie title
      const listItem = $('<li>').text(title);
      // Appends the new list item to the UL#list_movies
      $('UL#list_movies').append(listItem);
    });
  });
});
