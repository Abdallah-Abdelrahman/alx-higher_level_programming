$(document).ready(() => {
  console.log($('header'));
  $('div#red_header').on('click', (_evt) => $('header').addClass('red'));
});
