import pandas as pd
import os


def load_movies_data():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data')
    movies_df = pd.read_csv(os.path.join(data_path, 'tmdb_5000_movies.csv'))
    return movies_df.to_dict('records')

def load_credits_data():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data')
    credits_df = pd.read_csv(os.path.join(data_path, 'tmdb_5000_credits.csv'))
    return credits_df.to_dict('records')


movies_data = load_movies_data()
credits_data = load_credits_data()


