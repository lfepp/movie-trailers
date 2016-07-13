# Define Movie class
class Movie():
    """Creates a new Movie object

    Attributes:
        title (str): The title of the movie
        year (int): The year the movie was released
        poster_image_url (str): The address of a poster image for the movie
        trailer_youtube_url (str): The YouTube address of the movie's trailer
    """

    def __init__(self, title, year, poster_image_url, trailer_youtube_url):
        self.title = title
        self.year = year
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
