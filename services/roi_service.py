from .data_loader import movies_data
import json

def get_roi_by_country():
    movies = movies_data
    country_data = _process_roi_by_category(movies, "production_countries")

    return {
        country: _map_roi_data(rois)
        for country, rois in country_data.items()
    }

def get_roi_by_genre():
    movies = movies_data
    genre_data = _process_roi_by_category(movies, "genres")

    return {
        genre: _map_roi_data(rois)
        for genre, rois in genre_data.items()
    }

def _process_roi_by_category(movies, category_key):
    category_data = {}
    for movie in movies:
        if movie.get("budget", 0) > 0:
            roi = movie["revenue"] / movie["budget"]

            categories = movie.get(category_key, "[]")
            categories = json.loads(categories)

            for category_obj in categories:
                category_name = category_obj.get("name", "Unknown")

                if category_name not in category_data:
                    category_data[category_name] = []
                category_data[category_name].append(roi)

    return category_data

def _map_roi_data(roi_data):
    return {
        "average_roi": sum(roi_data) / len(roi_data),
        "count": len(roi_data)
    }


