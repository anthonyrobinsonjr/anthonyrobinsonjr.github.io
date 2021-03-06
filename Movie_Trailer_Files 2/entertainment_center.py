import fresh_tomatoes
import media

Toy_Story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", # noqa
                        "https://www.youtube.com/watch?v=27EzuAobbi0")

Avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", # noqa
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

Teenage_Mutant_Ninja_Turtles = media.Movie("tmnt",
                   "The turtles must confront an even greater nemisis",
                   "http://www.impawards.com/2014/posters/teenage_mutant_ninja_turtles_ver17.jpg", # noqa
                    "https://www.youtube.com/watch?v=HeaugHGd1Kw")

#tmnt.show_trailer()

Lion_King = media.Movie("lion_king",
                   "The adventures of a young lion who must thwart his \
                   uncle's attempts to take over the pride land",
                   "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg", # noqa
                    "https://www.youtube.com/watch?v=4sj1MT05lAA")

Pursuit_of_Happyness = media.Movie("pursuit_of_happyness",
                   "A biographical film of one man's struggle and perseverance",
                   "http://www.gstatic.com/tv/thumb/movieposters/162523/p162523_p_v8_ad.jpg", # noqa
                    "https://www.youtube.com/watch?v=89Kq8SDyvfg")

Planet_of_Apes = media.Movie("planet_of_apes",
                   "An astronaut crew crash lands on a planet in the distant \
                   future where intelligent talking apes are the dominant \
                   species, and humans are the oppressed and enslaved",
                   "http://stuffpoint.com/soundtracks/image/276594-soundtracks-rise-of-the-planet-of-the-apes-soundtrack-cover.jpg", # noqa
                    "https://www.youtube.com/watch?v=f8D2NIGEJW8")

Independence_Day = media.Movie("independence_day",
                   "The aliens are coming and their goal is to invade and \
                   destroy Earth. Fighting superior technology, mankind's \
                   best weapon is the will to survive",
                   "http://4.bp.blogspot.com/_VztDoszMydk/TP4lrunT74I/AAAAAAAAATc/m4yVZzkrg3Y/s1600/bfe94a73a587.png", # noqa
                    "https://www.youtube.com/watch?v=kA2WzBi2grE")

Taken = media.Movie("taken",
                   "A retired CIA agent travels across Europe and relies on \
                   his old skills to save his estranged daughter, who has been \
                   kidnapped while on a trip to Paris",
                   "http://www.counter-currents.com/wp-content/uploads/2010/08/taken-poster.jpg", # noqa
                    "https://www.youtube.com/watch?v=kZ02_Uzf7So")

movies = [Toy_Story, Avatar, Teenage_Mutant_Ninja_Turtles, Lion_King, 
          Pursuit_of_Happyness, Planet_of_Apes, Independence_Day, Taken]

fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)

