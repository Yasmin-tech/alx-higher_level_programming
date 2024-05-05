/*  a JavaScript script that fetches and lists the title for all movies from this URL:
 *  https://swapi-api.alx-tools.com/api/films/?format=json
 *  All movie titles will be list in the HTML tag UL#list_movies
 */

$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'get',
    success: function (data) {
      const results = data.results;
      $.each(results, function (i, result) {
        $('ul#list_movies').append('<li>' + result.title + '</li>');
      });
    }
  });
});
