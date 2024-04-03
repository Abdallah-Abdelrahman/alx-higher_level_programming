$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data, status) => {
    console.log({ data, status });
    if (status === 'success') {
      for ({ title } of data.results) {
        $('#list_movies').append(`<li>${title}</li>`);
      }
    }
  });
});
