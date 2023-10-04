<!DOCTYPE html>
<html lang="en">
<head>
  <title>Holberton School</title>
  <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  <script type="text/javascript">
    $(document).ready(function() {
      function fetchTranslation() {
        const languageCode = $('#language_code').val();
        const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
        
        $.get(apiUrl, function(data) {
          $('#hello').text(data.hello);
        });
      }

      $('#btn_translate').click(fetchTranslation);

      $('#language_code').keypress(function(event) {
        if (event.which === 13) { // Check if Enter key (key code 13) is pressed
          fetchTranslation();
        }
      });
    });
  </script>
</head>
<body>
  <header> 
    Say Hello
  </header>
  <br />
  <input id="language_code" type="text" placeholder="Language code"/>
  <input id="btn_translate" type="button" value="Translate"/>
  <br />
  <div id="hello"></div>
  <br />
  <footer>
    Holberton School - 2017
  </footer>
</body>
</html>
