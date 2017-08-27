import media #hold the Movie class to create new movie instances
import fresh_tomatoes #holds the open_movies_page which creates and launches fresh_tomatoes.html

#Initiate movie_list to append new movie instances to list
movie_list = []

#create list of favorite movies
lord_rings = media.Movie(
	"Lord of the Rings", 
	"https://upload.wikimedia.org/wikipedia/en/thumb/8/87/Ringstrilogyposter.jpg/330px-Ringstrilogyposter.jpg", 
	"https://www.youtube.com/watch?v=V75dMMIW2B4"
	)
movie_list.append(lord_rings)

jump_street = media.Movie(
	"21 Jump Street", 
	"https://upload.wikimedia.org/wikipedia/en/9/93/21JumpStreetfilm.jpg", 
	"https://www.youtube.com/watch?v=RLoKtb4c4W0&t=24s"
	)
movie_list.append(jump_street)

stooges = media.Movie(
	"The Three Stooges", 
	"https://upload.wikimedia.org/wikipedia/en/7/74/The_Three_Stooges_poster.jpg", 
	"https://www.youtube.com/watch?v=bPFPW7O5Tq8"
	)
movie_list.append(stooges)

#call method and pass movie list to create and launch fresh_tomatoes.html in default browser
fresh_tomatoes.open_movies_page(movie_list)
