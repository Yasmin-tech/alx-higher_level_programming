/* a JavaScript script that fetches the character name from this URL:
 *  https://swapi-api.alx-tools.com/api/people/5/?format=json
 *  The name will be displayed in the HTML tag DIV#character
 *  using AJAX-related JQuery methods
 */

$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (character) {
      $('div#character').text(character.name);
    }
  });
});
