$(document).ready(function () {
  // Fetches the translation data from the URL
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Extracts the translation of "hello"
    const helloTranslation = data.hello;
    // This displays the translation in the DIV#hello
    $('DIV#hello').text(helloTranslation);
  });
});
