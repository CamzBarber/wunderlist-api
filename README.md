# Wunderlist API Python
Example functions on how to call the Wunderlist API in Python 3.6.

1. Install the 'requests' library in Python.
2. Go to the [Wunderlist Developer site](http://developer.wunderlist.com) and register your app. Create an appropiate name and description and set the app url and auth callback url to anything; I used http://localhost/ for both.
3. On the 'My Apps' screen, make a note of the Client ID and Access Token - click 'Create Access Token' to see this.
4. Go to the [Wunderlist site](https://www.wunderlist.com/), open your list and make a note of the integer at the end of the URL. e.g. https://www.wunderlist.com/#/lists/123456789 - this is the list ID.
5. Download or clone the [Wunderlist.py](Wunderlist.py) file and open it in your Python editor.
6. Input your access_token, client_id and list_id to the head of the file.
7. Run the example functions at the bottom of the document. 
