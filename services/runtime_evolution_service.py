from .data_loader import movies_data
from datetime import datetime

def get_runtime_evolution():
    movies = movies_data
    decade_data = {}

    for movie in movies:
        runtime = movie.get("runtime")
        release_date = movie.get("release_date")

        if not runtime or not release_date or runtime == 0:
            continue

        try:
            year = datetime.strptime(release_date, "%Y-%m-%d").year

            current_year = datetime.now().year
            if year < current_year - 50:
                continue

            decade = (year // 10) * 10

            if decade not in decade_data:
                decade_data[decade] = []
            decade_data[decade].append(runtime)

        except (ValueError, TypeError):
            continue

    result = {}
    for decade, runtimes in sorted(decade_data.items()):
        valid_runtimes = [
            float(r) for r in runtimes
            if r is not None and str(r).lower() != 'nan'
        ]

        if not valid_runtimes:
            continue

        runtimes_sorted = sorted(valid_runtimes)
        median = runtimes_sorted[len(runtimes_sorted) // 2]

        result[f"{decade}s"] = {
            "average_runtime": round(sum(valid_runtimes) / len(valid_runtimes), 2),
            "median_runtime": round(median, 2),
            "count": len(valid_runtimes)
        }

    return result