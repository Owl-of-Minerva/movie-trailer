import webbrowser


class Movie():
    '''
    The Movie() class defines a movie class that stores
    relevant information about the movie, including movie title,
    poster image and url to the trailer video
    '''
    def __init__(self, movie_title, poster_image, trailer_youtube):
        '''
        The constructor passes in and store the values
        for movie title, poster image and url to the trailer video
        '''
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
