/* a javascript script that uses JQuery API to append <li>Item</li> html element
 *  when the user clicks on the tag DIV#add_item
 *  The new element is added to UL.my_list
 */
$(document).ready(function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
});
