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
    watch_list = []
    watch_list.append(movie)
    user_data["watchlist"] = watch_list
    return user_data





# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

