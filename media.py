'''
creates the Movie class which receives three arguments
1. Title of the Movie
2. Link to the poster image of the Movie
3. YouTube Link to youtube trailer video
'''


class Movie:
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
