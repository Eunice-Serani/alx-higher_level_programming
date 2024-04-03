$(document).ready(function () {
  // Adds event listener for adding new item
  $('DIV#add_item').click(function () {
    // Creates a new <li> element
    const newItem = $('<li>').text('Item');
    // Appends the new <li> element to UL.my_list
    $('UL.my_list').append(newItem);
  });

  // Adds event listener for removing last item
  $('DIV#remove_item').click(function () {
    // This removes the last <li> element from UL.my_list
    $('UL.my_list li:last-child').remove();
  });

  // Adds event listener for clearing the list
  $('DIV#clear_list').click(function () {
    // This removes all <li> elements from UL.my_list
    $('UL.my_list').empty();
  });
});
