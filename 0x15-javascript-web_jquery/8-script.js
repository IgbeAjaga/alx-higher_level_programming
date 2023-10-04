<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript">
      $(document).ready(function() {
        $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
          const movies = data.results;
          const listMovies = $('#list_movies');

          $.each(movies, function(index, movie) {
            const listItem = $('<li></li>').text(movie.title);
            listMovies.append(listItem);
          });
        });
      });
    </script>
  </body>
</html>
