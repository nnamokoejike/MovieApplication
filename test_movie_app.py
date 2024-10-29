import pytest
import json
import os
import tempfile
from storage_json import StorageJson
from storage_csv import StorageCsv
from movie_app import MovieApp


@pytest.fixture
def json_storage():
    # Create a temporary JSON file for testing
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    storage = StorageJson(temp_file.name)
    yield storage
    temp_file.close()
    os.remove(temp_file.name)


@pytest.fixture
def csv_storage():
    # Create a temporary CSV file for testing
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    storage = StorageCsv(temp_file.name)
    yield storage
    temp_file.close()
    os.remove(temp_file.name)


@pytest.fixture
def sample_movie_data():
    return {"title": "Inception",
            "year": "2010",
            "rating": 8.8,
            "poster": "https://example.com/inception.jpg"
            }


# Tests for StorageJson
def test_json_add_movie(json_storage, sample_movie_data):
    json_storage.add_movie(**sample_movie_data)
    movies = json_storage.list_movies()
    assert sample_movie_data["title"] in movies
    assert movies[sample_movie_data["title"]]["Rating"] == sample_movie_data["rating"]


def test_json_delete_movie(json_storage, sample_movie_data):
    json_storage.add_movie(**sample_movie_data)
    json_storage.delete_movie(sample_movie_data["title"])
    movies = json_storage.list_movies()
    assert sample_movie_data["title"] not in movies


def test_json_update_movie(json_storage, sample_movie_data):
    json_storage.add_movie(**sample_movie_data)
    json_storage.update_movie(sample_movie_data["title"], 9.0)
    movies = json_storage.list_movies()
    assert movies[sample_movie_data["title"]]["Rating"] == 9.0


# Tests for StorageCsv
def test_csv_add_movie(csv_storage, sample_movie_data):
    csv_storage.add_movie(**sample_movie_data)
    movies = csv_storage.list_movies()
    assert sample_movie_data["title"] in movies
    assert movies[sample_movie_data["title"]]["Rating"] == sample_movie_data["rating"]


def test_csv_delete_movie(csv_storage, sample_movie_data):
    csv_storage.add_movie(**sample_movie_data)
    csv_storage.delete_movie(sample_movie_data["title"])
    movies = csv_storage.list_movies()
    assert sample_movie_data["title"] not in movies


def test_csv_update_movie(csv_storage, sample_movie_data):
    csv_storage.add_movie(**sample_movie_data)
    csv_storage.update_movie(sample_movie_data["title"], 9.0)
    movies = csv_storage.list_movies()
    assert movies[sample_movie_data["title"]]["Rating"] == 9.0


# Tests for MovieApp
def test_movie_app_list_movies(json_storage, sample_movie_data):
    app = MovieApp(json_storage)
    json_storage.add_movie(**sample_movie_data)
    movies = app._storage.list_movies()
    assert sample_movie_data["title"] in movies


def test_movie_app_add_movie(json_storage, sample_movie_data):
    app = MovieApp(json_storage)
    app._storage.add_movie(**sample_movie_data)
    movies = json_storage.list_movies()
    assert sample_movie_data["title"] in movies


def test_movie_app_delete_movie(json_storage, sample_movie_data):
    app = MovieApp(json_storage)
    app._storage.add_movie(**sample_movie_data)
    app._storage.delete_movie(sample_movie_data["title"])
    movies = json_storage.list_movies()
    assert sample_movie_data["title"] not in movies
