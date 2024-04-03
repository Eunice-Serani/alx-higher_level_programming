// Waits for the document to be ready
$(document).ready(function () {
  // Adds a click event listener to the DIV#toggle_header
  $('DIV#toggle_header').click(function () {
    // Checks if the <header> element has class 'red'
    if ($('header').hasClass('red')) {
      // If it has class 'red', toggle to 'green'
      $('header').removeClass('red').addClass('green');
    } else {
      // If it doesn't have class 'red', toggle to 'red'
      $('header').removeClass('green').addClass('red');
    }
  });
});
