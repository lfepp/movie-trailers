import media
import fresh_tomatoes

# Define instances of Movie
heathers = media.Movie("Heathers", 1988, "http://i.imgur.com/kFZHdMf.jpg",
                       "https://www.youtube.com/watch?v=hf6OhBKksKg")
kiss_kiss_bang_bang = media.Movie("Kiss Kiss Bang Bang", 2005,
                                  "http://i.imgur.com/300oQl0.jpg",
                                  "https://www.youtube.com/watch?v=Q-ekNtkhLjs"  # NOQA
                                  )
big_lebowski = media.Movie("The Big Lebowski", 1998,
                           "http://i.imgur.com/TdWkmR3.jpg",
                           "https://www.youtube.com/watch?v=B6s60JdiHJc")
shawshank = media.Movie("The Shawshank Redemption", 1994,
                        "http://i.imgur.com/kbeoCpU.jpg",
                        "https://www.youtube.com/watch?v=K_tLp7T6U1c")

# Define list of movies
movies = [heathers, kiss_kiss_bang_bang, big_lebowski, shawshank]

# Initialize open_movies_page
if __name__ == "__main__":
    fresh_tomatoes.open_movies_page(movies)
