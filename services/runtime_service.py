from .util import generate_response

FILE_ARTIFACTS_DIR = "runtime_evolution.json"


def get_runtime_evolution() -> dict:
    return generate_response(FILE_ARTIFACTS_DIR)
