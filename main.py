import argparse
import os
from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv


def main():
    # Set up argument parser

    parser = argparse.ArgumentParser(description="Run the movie app with a specified storage file.")
    parser.add_argument("file_path", help="Path to the storage file (e.g., vin.json or onyi.csv)")

    # Parse command-line arguments
    args = parser.parse_args()
    file_path = args.file_path
    _, file_extension = os.path.splitext(file_path)
    if file_extension == ".json":
        storage = StorageJson(file_path)
    elif file_extension == ".csv":
        storage = StorageCsv(file_path)
    else:
        print("Unsupported file format. Please use a .json or .csv file.")
        return

    # Initialize  the movie app
    movie_app = MovieApp(storage)

    # Run the app.
    movie_app.run()


if __name__ == "__main__":
    main()
