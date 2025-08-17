movies = [
    {"title": "Inception", "ratings": [9, 8, 10]},
    {"title": "Titanic", "ratings": [7, 8, 7]},
    {"title": "Avatar", "ratings": [8, 9, 8]}
]
from pprint import pprint
def movie_report(movies):
    final_output = {}
    for movie in movies:
        avg_rating = sum(movie["ratings"]) / len(movie["ratings"])
        status = "Hit" if avg_rating >= 8.5 else "Average"
        final_output[movie["title"]] = {
            "average_rating": round(avg_rating, 1),
            "status": status
        }
    return final_output

pprint(movie_report(movies))
