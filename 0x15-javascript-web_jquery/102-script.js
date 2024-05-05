/*  a JavaScript script that fetches and prints how to say “Hello” depending on the language
 *     From API service: https://www.fourtonfish.com/hellosalut/hello/
 *     The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
 *     The translation must be fetched when the user clicks on INPUT#btn_translate
 *     The translation of “Hello” must be displayed in the HTML tag DIV#hello
 *     Using the JQuery API
 */

$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const languageCode = $('input#language_code').val();
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode,
      method: 'get',
      success: function (data) {
        $('div#hello').text(data.hello);
      }
    });
  });
});
