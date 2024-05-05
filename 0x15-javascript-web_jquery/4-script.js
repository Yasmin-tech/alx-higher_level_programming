/* a javascript script that uses JQuery API to toggles the color of the header between red and green
 * when we click on the div with toggle_header ID */

$(document).ready(function () {
  $('div#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
