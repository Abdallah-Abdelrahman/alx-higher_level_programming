$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data, status) => {
    console.log({ data, status });
    if (status === 'success') {
      $('div#character').text(data.name);
    }
  });
});
