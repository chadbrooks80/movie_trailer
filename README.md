# Movie Trailer Website
`Movie Trailer Website` is a Python application that creates a website (html file) which displays your favorite movies.  Features include allowing you to display your movies on a responsive website with a large title, poster image, and a pop-up movie trailer display from YouTube. 

## Running the app app
To have the website created and automatically launched on your default browser, you will need to run the following: 
```
python entertainment_center.py
```
## Files included
`Movie Trailer Website` includes the following files:
*  `entertainment_center.py` - This is the main python module that must be ran with either version 2 or 3 of Python.
*  `media.py` - This module holds the Movie class, which allows you to create new instances of movies you would like to be displayed. This module must be included within the `entertainment_center.py` module.
*  `fresh_tomatoes.py` - This module includes code for creating and launching the website. It must be included within `entertainment_center.py` module.
*  `fresh_tomatoes.html` - This is the main website file that is created and launched after running the `entertainment_center.py` module.  All styling and scripting is included within this file.  

## Adding/Modifying Movies
Modifying or adding additional movies within `Movie Trailer Website` requires two steps within `entertainment_center.py`: 
1. Creating a new instance of the Movie class which takes three arguments:
    1. The title of the movie
    2. A link to the poster image of the movie
    3. A link to the YouTube trailer

    Here is an example:
    ```
    lord_flies = Movie(
        "Lord of the Flies", 
        "https://en.wikipedia.org/wiki/File:Lord_of_the_Flies_(1990_film).jpg"
        "https://www.youtube.com/watch?v=QnCn2VTzY90"
        )
    ```
2. Adding the new Movie instance to `movie_list`:
    ```
    movie_list.append(lord_flies)
    ```

## Supported Python Versions
`Movie Trailer Website` has been tested and working on both Python versions 2 and 3.

## Licensing
`Movie Trailer Website` is a public domain work, dedicated using [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Feel free to do whatever you want with it.
