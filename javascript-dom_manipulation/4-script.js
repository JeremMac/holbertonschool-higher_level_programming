document.addEventListener('DOMContentLoaded', function () {
  const item = document.querySelector('#add_item');
  const MyList = document.querySelector('.my_list');
  item.addEventListener('click', function () {
    const NewItem = document.createElement('li');
    NewItem.textContent = 'Item';
    MyList.appendChild(NewItem);
  });
});
