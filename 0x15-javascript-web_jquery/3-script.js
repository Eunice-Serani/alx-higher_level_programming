// Waits for the document to be ready
$(document).ready(function () {
  // Adds a click event listener to the DIV#red_header
  $('DIV#red_header').click(function () {
    // Adds the class 'red' to the <header> element
    $('header').addClass('red');
  });
});
