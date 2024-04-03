$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data, status) => {
    console.log({ data, status });
    if (status === 'success') {
      $('#hello').text(data.hello);
    }
  });
});
