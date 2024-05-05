/* A javascript script that updates the header to 'New Header!!!'
 *    on the click of div with ID 'update_header' using JQuery API
 */

$(document).ready(function () {
  $('div#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
