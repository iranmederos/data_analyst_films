from .util import generate_response

FILE_ARTIFACTS_DIR = "budget_rating_corr.json"


def get_budget_rating_corr() -> dict:
    return generate_response(FILE_ARTIFACTS_DIR)
