$(document).ready(() => {
  const header = $('header');
  console.log({ header });
  $('div#update_header').click((_evt) => $('header').text('New Header!!!'));
});
