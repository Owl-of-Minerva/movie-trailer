import media
import fresh_tomatoes


# instantiate movie objects by calling movie constructors
it = media.Movie(
    "it",
    "https://upload.wikimedia.org/wikipedia/en/5/5a/It_(2017)_poster.jpg",    # NOQA
    "https://www.youtube.com/watch?v=xKJmEC5ieOk")

dunkirk = media.Movie(
    "Dunkirk",
    "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",    # NOQA
    "https://www.youtube.com/watch?v=T7O7BtBnsG4")

wonder_woman = media.Movie(
    "Wonder Woman",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_(2017_film).jpg",    # NOQA
    "https://www.youtube.com/watch?v=F0lZgaz0CIE")

ghost_in_the_shell = media.Movie(
    "Ghost in the Shell",
    "https://upload.wikimedia.org/wikipedia/en/1/11/Ghost_in_the_Shell_(2017_film).png",    # NOQA
    "https://www.youtube.com/watch?v=QwwHJSmOHfA")

american_assassin = media.Movie(
    "American Assassin",
    "https://upload.wikimedia.org/wikipedia/en/5/5d/American_Assassin.jpg",    # NOQA
    "https://www.youtube.com/watch?v=745tOzSXc4I")

wind_river = media.Movie(
    "Wind River",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Wind_River_(2017_film).png",    # NOQA
    "https://www.youtube.com/watch?v=zN9PDOoLAfg")

# store movie objects into a list
movies = []
movies.append(it)
movies.append(dunkirk)
movies.append(wonder_woman)
movies.append(ghost_in_the_shell)
movies.append(american_assassin)
movies.append(wind_river)
# call the function to generate the static webpage
fresh_tomatoes.open_movies_page(movies)
