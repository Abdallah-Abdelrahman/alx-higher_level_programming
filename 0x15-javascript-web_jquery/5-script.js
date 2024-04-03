$(document).ready(() => {
  const header = $('header');
  console.log({ header });
  $('div#add_item').click((_evt) => $('ul.my_list').append('<li>Item</li>'));
});
