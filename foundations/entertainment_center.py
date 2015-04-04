import media
import fresh_tomatoes
"""Creates 6 instances of the media class Movie for each of my favorite movies!!!"""
modern_times = media.Movie("Modern Times",
						   "A man struggles to adjust to modern life",
						   "http://upload.wikimedia.org/wikipedia/en/6/6e/Moderntimes.jpg",
						   "https://www.youtube.com/watch?v=2B3HGY_zLKk",
						   1936)

river_kwai = media.Movie("the Bridge on the River Kwai",
						 "A story of a platoon building a bridge",
						 "http://upload.wikimedia.org/wikipedia/en/f/f2/The_Bridge_on_the_River_Kwai_poster.jpg",
						 "https://www.youtube.com/watch?v=SFMmJMNRv-Q",
						 1952)

gentlemen_prefer_blondes = media.Movie("Gentlemen Prefer Blondes",
						 "A story about two woman on a boat",
						 "http://upload.wikimedia.org/wikipedia/en/3/32/Gentlemen_Prefer_Blondes_%281953%29_film_poster.jpg",
						 "https://www.youtube.com/watch?v=ur9GKLl8v4U",
						 1953)

blues_brothers = media.Movie("The Blue's Brothers",
							 "A story about two brothers saving an orphanage",
							 "http://upload.wikimedia.org/wikipedia/en/a/ae/Bluesbrothersmovieposter.jpg",
							 "https://www.youtube.com/watch?v=A-xtJYIwfYo",
							 1980)

shawshank_redemption = media.Movie("The Shawshank Redemption",
								   "A man escapes from prison",
								   "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
								   "https://www.youtube.com/watch?v=NmzuHjWmXOc",
								   1994)

gaurdians_of_the_galaxy = media.Movie("Gaurdians of the Galaxy",
									  "A bunch of misfits save the universe",
									  "http://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
									  "https://www.youtube.com/watch?v=B16Bo47KS2g",
									  2014)


# Stores my objects as a list

movies = [modern_times, river_kwai, gentlemen_prefer_blondes, blues_brothers, shawshank_redemption, gaurdians_of_the_galaxy]

#runs the function open movies page from the fresh_tomatoes files
fresh_tomatoes.open_movies_page(movies)

#pritns information about the functions being run to the terminal
print(media.Movie.__doc__)
print(media.Movie.__name__+ " is the name of the class being called.")
print(media.Movie.__module__+ " is the name of the module the class is defined in.")