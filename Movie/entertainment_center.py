import media
import fresh_tomatoes

# Fav movies trailors are created in the form of instances
avengers = media.Movie("Avengers Age of Ultron",
                       "A Superhero flim "
                       "heros like ironman,thor,captain America",
                       "https://hcmoviereviews.files.wordpress.com"
                       "/2015/04/avengers-age-of-ultron-uk-poster.jpg",  # noqa
                       "https://www.youtube.com/watch?v=JAUoeqvedMo")  # noqa
ironman = media.Movie("Ironman 3",
                      "When Tony Stark worls is destroyed "
                      "by an terroist mandarinHe starts an "
                      "oddessy of rebuilding and retribution ",
                      "http://cdn.collider.com/wp-content/uploads"
                      "/iron-man-3-international-poster.jpg",   # noqa
                      "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")  # noqa

mesaya_muruku = media.Movie("Mesaya Muruku",
                            "A semi biopic of Hiphop tamizha"
                            "how he become an succesful music director",
                            "https://dhoom.filmipop.com/media//movie/2016"
                            "/Nov/1478580034-Meesaya-Murukku.jpg",  # noqa
                            "https://www.youtube.com/watch?v=Ghizg_3uI3E")

the_great_gatsby = media.Movie("The Great Gatsby",
                               "A Writer and a wall street trader nick,"
                               "himself drawn to the past and his life "
                               "style by a neighbour millionaire gatsby.",
                               "http://www.impawards.com/2013/posters"
                               "/great_gatsby_ver15_xlg.jpg",  # noqa
                               "https://www.youtube.com/watch?v=rARN6agiW7o")

baywatch = media.Movie("Baywatch",
                       "Devoted lifeguard Mitch Buchannon butts "
                       "heads with a brash new recruit,"
                       "as they uncover a criminal "
                       "plot that threatens the future of the bay.",
                       "http://www.impawards.com/2017/posters"
                       "/baywatch_ver15_xlg.jpg",  # noqa
                       "https://www.youtube.com/watch?v=GvVY0AfrOiw")  # noqa
art = media.Movie("Box art",
                  "Diagonal art program Using python programming",
                  "art.PNG",  # noqa
                  "https://www.youtube.com/watch?v=biOx_tBm5dE")  # noqa
# All instances are added to a list
movies = [avengers, ironman, mesaya_muruku, the_great_gatsby, baywatch, art]
fresh_tomatoes.open_movies_page(movies)
