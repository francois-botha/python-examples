# About the program:
# Inside it, define a list of Strings of your 5 favourite movies. 
# Now, loop over the list. For each item in the list, print out "Movie: " plus the movies name.
# Can you figure out how to print out Movie 1: <Movie 1's name>. Movie 2: ...etc?
# HINT: YOU WILL NEED TO LOOK UP the 'enumerate' command in Python using a Google search. This command allows you to loop over a list
# retaining both the item at every position and its index (i.e. position in the list).

# Define a list for movies with values
movieList = ["BumbleBee", "Transformers", "Die Hard 4.0", "Need for Speed", "Journey to the Center of the Earth"]

for counter, movie in enumerate(movieList, 1) : 
    print(f"Movie {counter}: {movie}")