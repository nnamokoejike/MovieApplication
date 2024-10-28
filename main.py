# import requests
#
# user_dict = {"email":"mail@sdasdd.com","password":"Pass123123","passwordRepeat":"Pass123123","securityQuestion":{"id":5,"question":"Maternal grandmother's first name?","createdAt":"2023-05-16T06:14:15.528Z","updatedAt":"2023-05-16T06:14:15.528Z"},"securityAnswer":"dasdd"}
# response = requests.post('https://juice-shop.herokuapp.com/api/Users/', json=user_dict)
# print(response.status_code)
# print(response.text)


from movie_app import MovieApp
from storage_csv import StorageCsv


def main():
    # Create an instance of StorgeJson with the specific file path.
    storage = StorageCsv('movies.csv')

    # Create an instance of the MovieApp with the JSON storage.
    movie_app = MovieApp(storage)

    # Run the app.
    movie_app.run()


if __name__ == "__main__":
    main()
