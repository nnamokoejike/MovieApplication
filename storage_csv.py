import csv
from istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path):
        """
        Initialize the StorageCsv with a file path.
        :param file_path: Path to CSV file where movie data is stored.
        """
        self.file_path = file_path

    def list_movies(self):
        """
        Reads movies from the CSV file and returns a dictionary of dictionaries.
        :return: A dictionary where keys are movie titles, and values are dictionaries
                 containing the movie's rating, year, and poster URL.
        """

        movies = {}
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row['title']  # Correctly access the title
                    movies[title] = {
                        "Rating": float(row['rating']),
                        "Year of release": row['year'],
                        "Poster Image URL": row['poster']
                    }
        except FileNotFoundError:
            # Return an empty dictionary if the file does not exist.
            pass

        return movies

    def add_movie(self, title, year, rating, poster):
        """
        Add a new movie to the CSV storage.

        :param title: Title of the movie.
        :param year:  Year of release.
        :param rating: Rating of the movie.
        :param poster: URl of the movie's poster.
        """

        movies = self.list_movies()
        movies[title] = {
            "Rating": rating,
            "Year of release": year,
            "Poster Image URL": poster
        }
        self._save_to_file(movies)

    def delete_movie(self, title):
        """
        Deletes a movie from the CSV storage.
        :param title: Title of the movie to delete.
        """
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_to_file(movies)
            print(f"{title} successfully deleted!")
        else:
            print(f"{title} not found in the database.")

    def update_movie(self, title, rating):
        """
        Updates the rating of a movie in the CSV storage.
        :param title: Title of the movie in the CSV storage.
        :param rating: New rating of the movie.
        """

        movies = self.list_movies()
        if title in movies:
            movies[title]["Rating"] = rating
            self._save_to_file(movies)
            print(f"Rating for {title} updated to {rating}.")
        else:
            print(f"{title} not found in the database.")

    def _save_to_file(self, movies):
        """
        Saves the movies dictionary back to the CSV file.
        :param movies: A dictionary of movie data to save.
        """

        with open(self.file_path, 'w', newline='') as file:
            fieldnames = ['title', 'rating', 'year', 'poster']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for title, details in movies.items():
                writer.writerow({
                    'title': title,
                    'rating': details["Rating"],
                    'year': details["Year of release"],
                    'poster': details["Poster Image URL"]
                })
