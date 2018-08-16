
class Movie:
    """This class defines the key attributes which are necessary for a
movie description"""
    def __init__(self, title, movie_storyline, poster_image, trailer_youtube):
        """This is constructor, used for initiliziing the instance variables.
        Args:
        It takes five arguments to make it work.
        self:It is the default argument.
        title:Title of the movie.
        movie_storyline:About the movie.
        poster_image:Poster of the image.
        trailer_youtube:Youtube trailer of the movie."""
        self.title = title
        storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
