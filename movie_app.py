class MovieApp:
    def __init__(self, storage):
        """
        Initialize the MovieApp with a storage object.
        :param storage: An instance of a class implementing the IStorage interface.
        """
        self._storage = storage

    def _command_list_movies(self):
        """Lists all movies in the storage."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies in the database.")
        else:
            for title, details in movies.items():
                print(f"{title}: {details['Rating']}, {details['Year of release']}")

    def _command_add_movie(self):
        """Adds a movie to the storage."""
        title = input("Enter the movie title: ")
        year = input("Enter the year of release: ")
        rating = float(input("Enter the movie rating: "))
        poster = input("Enter the URL for the poster image: ")
        self._storage.add_movie(title, year, rating, poster)
        print(f"Movie '{title}' successfully added.")

    def _command_delete_movie(self):
        """Deletes a movie from the storage."""
        title = input("Enter the movie title to delete: ")
        self._storage.delete_movie(title)

    def _command_update_movie(self):
        """Updates the rating of a movie in the storage."""
        title = input("Enter the movie title to update: ")
        rating = float(input("Enter the new rating: "))
        self._storage.update_movie(title, rating)

    def _command_movie_stats(self):
        """Displays statistics about the movies in storage."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies in the database to analyze.")
            return

        ratings = [details['Rating'] for details in movies.values()]
        avg_rating = sum(ratings) / len(ratings)
        sorted_ratings = sorted(ratings)
        median_rating = (
            sorted_ratings[len(sorted_ratings) // 2]
            if len(sorted_ratings) % 2 != 0
            else (sorted_ratings[len(sorted_ratings) // 2 - 1] + sorted_ratings[len(sorted_ratings) // 2]) / 2
        )

        best_movie = max(movies, key=lambda title: movies[title]['Rating'])
        worst_movie = min(movies, key=lambda title: movies[title]['Rating'])

        print(f"Average rating: {avg_rating:.2f}")
        print(f"Median rating: {median_rating:.2f}")
        print(f"Best movie: {best_movie} with a rating of {movies[best_movie]['Rating']}")
        print(f"Worst movie: {worst_movie} with a rating of {movies[worst_movie]['Rating']}")

    def _generate_website(self):
        """Generates a website from the movie data."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies to generate a website.")
            return

        with open("index.html", "r") as template_file:
            template_content = template_file.read()

        movie_items = ""
        for title, details in movies.items():
            movie_items += (
                f"<li><div class='movie'><img class='movie-poster' src='{details['Poster Image URL']}'>"
                f"<div class='movie-title'>{title}</div>"
                f"<div class= 'movie-year'>{details['Year of release']}</div></div></li>\n"
            )

        output_content = template_content.replace("__TEMPLATE_MOVIE_GRID__", movie_items)

        with open("index.html", "w") as output_file:
            output_file.write(output_content)

        print("Website generated successfully as 'index.html'.")

    def run(self):
        """Runs the movie app and handles user inout."""
        while True:
            print("""
            **********My Movies Database ************
            
            Menu:
            0. Exit
            1. List movies
            2. Add movie
            3. Delete movie
            4. Update movie
            5. Stats
            6. Generate website
            """)
            choice = input("Enter choice (0-6): ").strip()
            if choice == "0":
                print("Exiting... Goodbye!")
                break
            elif choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_add_movie()
            elif choice == "3":
                self._command_delete_movie()
            elif choice == "4":
                self._command_update_movie()
            elif choice == "5":
                self._command_movie_stats()
            elif choice == "6":
                self._generate_website()
            else:
                print("Invalid choice, please try again.")

            input("\nPress Enter to continue...")
