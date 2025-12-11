from .util import generate_response

FILE_ARTIFACTS_DIR_GENRE = "roi_by_genre.json"
FILE_ARTIFACTS_DIR_COUNTRY = "roi_by_country.json"


def get_roi_by_genre() -> dict:
    return generate_response(FILE_ARTIFACTS_DIR_GENRE)


def get_roi_by_country() -> dict:
    return generate_response(FILE_ARTIFACTS_DIR_COUNTRY)
