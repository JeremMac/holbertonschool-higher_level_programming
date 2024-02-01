document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const helloTranslation = data.hello;
      document.getElementById('hello').textContent = helloTranslation;
    })
    .catch(error => {
      console.log('Error fetching hello translation:', error);
    });
});
