document.addEventListener('DOMContentLoaded', function () {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      data.results.forEach(film => {
        const movieTitle = film.title;
        const listMovies = document.querySelector('#list_movies');
        const newListItem = document.createElement('li');
        newListItem.textContent = movieTitle;
        listMovies.appendChild(newListItem);
      });
    })
    .catch((error) => {
      console.log('Error fetching movie titles:', error);
    });
});
