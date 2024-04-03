$(document).ready(() => {
  $('input#btn_translate').click(_evt => {
    lang = $('input#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (data, status) => {
      if (status === 'success') {
        $('div#hello').text(data.hello);
      }
    });
  });
});
