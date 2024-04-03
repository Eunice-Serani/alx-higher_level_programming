// Waits for the document to be ready
$(document).ready(function () {
  // Adds a click event listener to the DIV#red_header
  $('DIV#red_header').click(function () {
    // Updates the text color of the <header> element to red
    $('header').css('color', '#FF0000');
  });
});
