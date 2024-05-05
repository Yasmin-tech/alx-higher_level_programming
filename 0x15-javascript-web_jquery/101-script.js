/* a JavaScript script that adds, removes and clears LI elements from a UL list when the user clicks:
 * DIV#add_item: a new element is added to the list,
 * DIV#remove_item: the last element is removed from the list
 * DIV#clear_list: all elements of the list are removed
 *     Using JQuery API
 */

$(document).ready(function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('div#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  $('div#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
