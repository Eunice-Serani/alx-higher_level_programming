// Waits for the document to be ready
$(document).ready(function () {
  // Adds a click event listener to the DIV#add_item
  $('DIV#add_item').click(function () {
    // Creates a new <li> element
    const newItem = $('<li>Item</li>');
    // Appends the new <li> element to the UL.my_list
    $('ul.my_list').append(newItem);
  });
});
