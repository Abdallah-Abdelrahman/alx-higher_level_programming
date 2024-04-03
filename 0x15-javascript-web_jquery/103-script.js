$(document).ready(() => {
  $('input#btn_translate').click(_evt => {
    lang = $('input#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (data, status) => {
      if (status === 'success') {
        $('div#hello').text(data.hello);
      }
    });
  });

  // when user focus and press enter on input field
  $('input#language_code').focus(evt => {
    evt.target.addEventListener('keypress', evt => {
      const code = (evt.keyCode ? evt.keyCode : evt.which) === 13;
      if (code) {
        lang = $('input#language_code').val();
        $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (data, status) => {
          if (status === 'success') {
            $('div#hello').text(data.hello);
          }
        });
      }
    });
  });
});
