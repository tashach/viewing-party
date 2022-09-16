# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating:
        movie['title'] = title
        movie['genre'] = genre
        movie['rating'] = rating
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    watched_movies = []
    watched_movies.append(movie)
    user_data["watched"] = watched_movies
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = []
    watchlist.append(movie)
    user_data["watchlist"] = watchlist
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = 0
    average_rating = 0
    if user_data["watched"]:
        for movie in user_data["watched"]:
            ratings += movie["rating"]
        average_rating = ratings/ len(user_data["watched"])
    return average_rating


def get_most_watched_genre(user_data):
    watched_genres = {}
    most_watched_count = 0

    if user_data["watched"]:
        for movie in user_data["watched"]:
            if movie["genre"] not in watched_genres:
                watched_genres[(movie["genre"])] = 1
            else:
                watched_genres[(movie["genre"])] += 1
        
        for genre, count in watched_genres.items():
            if count > most_watched_count:
                most_watched_count = count
                most_watched_genre = genre
  
        return most_watched_genre

    else:
        return None

    



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

