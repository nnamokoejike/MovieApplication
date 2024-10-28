from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """Returns a dictionary of movies."""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """Adds a new movie to the storage."""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """Deletes a movie from the storage."""
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """Update a movie's rating in the storage"""
        pass
