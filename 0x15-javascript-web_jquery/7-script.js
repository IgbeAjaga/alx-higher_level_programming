<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript">
      $(document).ready(function() {
        $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
          $('#character').text(data.name);
        });
      });
    </script>
  </body>
</html>
