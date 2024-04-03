$(document).ready(() => {
  const item = '<li>Item</li>';

  function handler (action) {
    return function eventHandler (_evt) {
      switch (action) {
        case 'add':
          $('.my_list').append(item);
          break;
        case 'remove':
          $('.my_list li').last().remove();
          break;
        case 'clear':
          $('.my_list li').remove();
          break;
      }
    };
  }

  $('#add_item').click(handler('add'));
  $('#remove_item').click(handler('remove'));
  $('#clear_list').click(handler('clear'));
});
