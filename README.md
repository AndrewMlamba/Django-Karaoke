# Welcome to Django-Karaoke!

We're going to put on a Karaoke party at our next Django conference and we need to prototype an app for it. I've included a basic bit of HTML and some tests but I'll need you to finish up the code in the `songs` app. Thanks for helping out!

Here are some details:

## Song model should:
* [x] have a title
* [x] have an artist (original performer)
* [x] have a performer (who's singing it for karaoke) (make this another model)
* [x] have a length (number of seconds in duration)
* [x] return `'<title> by <artist>'` when turned into a string
  
## Performer model should:
- [x] have a name
- [x] return the name when turned into a string
  
## Views:
- [x] list view, all of the songs
- [x] detail view, a particular song
    * `tell who's performing it`
- [x] performer view, a particular performer
    * `list all of their songs`
    
Feel free to add other features, too, if you want. Like maybe the minutes:seconds version of how long the song is?

You can check out the tests in songs/tests.py and run them with `python manage.py tests`.

Good luck!
