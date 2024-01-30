const titleElement = document.querySelector('#red_header');
titleElement.addEventListener('click', () => {
  document.querySelector('header').classList.add('red');
});
