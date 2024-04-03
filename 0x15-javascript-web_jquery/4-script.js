$(document).ready(() => {
  const header = $('header');
  console.log({ header });
  $('div#toggle_header').click((_evt) => header.toggleClass('red green'));
});
