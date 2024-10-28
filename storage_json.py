import json

from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """Reads and returns all movies from the JSON file."""
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  # Return an empty dictionary if the file does not exist

    def add_movie(self, title, year, rating, poster):
        """Adds a new movie to the JSON storage."""
        movies = self.list_movies()
        movies[title] = {
            "Rating": rating,
            "Year of release": year,
            "Poster Image URL": poster
        }
        self._save_to_file(movies)

    def delete_movie(self, title):
        """Deletes a movie from the JSON storage."""
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_to_file(movies)
            print(f"{title} successfully deleted!")
        else:
            print(f"{title} not found in database.")

    def update_movie(self, title, rating):
        """Updates a movie's rating in the JSON storage."""
        movies = self.list_movies()
        if title in movies:
            movies[title]["Rating"] = rating
            self._save_to_file(movies)
            print(f"Rating for {title} updated to {rating}.")
        else:
            print(f"{title} not found in the database")

    def _save_to_file(self, movies):
        """Saves the movie data back to the JSON file."""
        with open(self.file_path, "w") as file:
            json.dump(movies, file, indent=4)
