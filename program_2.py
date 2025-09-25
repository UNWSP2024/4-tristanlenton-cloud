movies = True
tickets = 0
while movies:
    movie = input("Enter a movie title: ")
    tickets += int(input("Enter the number of tickets for this movie: "))
    moreMovies = input("Do you have more movies? (y/n): ")
    if moreMovies == "y":
        movies = True
    else:
        movies = False
print("Total number of tickets is", tickets)