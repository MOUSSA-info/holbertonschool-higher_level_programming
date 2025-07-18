document.getElementById('add_item').onclick = function () {
  const ul = document.querySelector('.my_list');
  const li = document.createElement('li');
  li.textContent = 'Item';
  ul.appendChild(li);
};
