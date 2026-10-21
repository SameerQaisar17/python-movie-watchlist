import json
import os

print("===== MOVIE WATCHLIST MANAGER =====")


def load_movies():
    if not os.path.exists("movies.json"):
        return []

    try:
        with open("movies.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return [
                movie for movie in data
                if isinstance(movie, dict)
                and isinstance(movie.get("title"), str)
                and isinstance(movie.get("watched"), bool)
            ]

        print("Warning: Movie data is invalid. Starting with an empty list.")
        return []

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved movies. Starting with an empty list.")
        return []


def save_movies():
    try:
        with open("movies.json", "w", encoding="utf-8") as file:
            json.dump(movies, file, indent=4, ensure_ascii=False)
        return True

    except OSError:
        print("Error: Could not save your movies.")
        return False


movies = load_movies()

while True:
    print("\n1. Add Movie")
    print("2. View Movies")
    print("3. Search Movie")
    print("4. Mark Movie as Watched")
    print("5. Delete Movie")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        title = input("Enter movie title: ").strip()

        if title:
            movies.append({"title": title, "watched": False})

            if save_movies():
                print(f"'{title}' added successfully!")
            else:
                print("Movie added for this session, but not saved to file.")
        else:
            print("Movie title cannot be empty.")

    elif choice == "2":
        if not movies:
            print("Your watchlist is empty.")
        else:
            print("\n===== YOUR MOVIES =====")

            for number, movie in enumerate(movies, start=1):
                status = "Watched" if movie["watched"] else "Not watched"
                print(f"{number}. {movie['title']} - {status}")

    elif choice == "3":
        search_title = input("Enter movie title to search: ").strip()

        if not search_title:
            print("Movie title cannot be empty.")
        else:
            found = False

            for movie in movies:
                if search_title.lower() in movie["title"].lower():
                    status = "Watched" if movie["watched"] else "Not watched"
                    print(f"{movie['title']} - {status}")
                    found = True

            if not found:
                print("Movie not found.")

    elif choice == "4":
        if not movies:
            print("Your watchlist is empty.")
        else:
            for number, movie in enumerate(movies, start=1):
                print(f"{number}. {movie['title']}")

            try:
                number = int(input("Enter movie number to mark as watched: "))

                if 1 <= number <= len(movies):
                    movie = movies[number - 1]

                    if movie["watched"]:
                        print("This movie is already marked as watched!")
                    else:
                        movie["watched"] = True

                        if save_movies():
                            print(f"'{movie['title']}' marked as watched!")
                        else:
                            print("Change made for this session, but not saved.")
                else:
                    print("Invalid movie number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        if not movies:
            print("Your watchlist is empty.")
        else:
            print("\n===== YOUR MOVIES =====")

            for number, movie in enumerate(movies, start=1):
                print(f"{number}. {movie['title']}")

            try:
                number = int(input("Enter movie number to delete: "))

                if 1 <= number <= len(movies):
                    deleted_movie = movies.pop(number - 1)

                    if save_movies():
                        print(f"'{deleted_movie['title']}' deleted successfully!")
                    else:
                        print("Movie deleted for this session, but not saved.")
                else:
                    print("Invalid movie number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option! Please choose 1-6.")