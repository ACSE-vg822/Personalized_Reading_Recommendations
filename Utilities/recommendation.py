import pandas as pd
from rapidfuzz import process
import pickle
import os
import joblib

def get_recommendations(title, threshold=80):

    # Get the current directory where this script is located (inside Utilities)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Move up one level to the parent directory
    base_dir = os.path.dirname(current_dir)

    # Build paths to File_dump directory, which is at the same level as Utilities
    file_dump_dir = os.path.join(base_dir, 'File_dump')

    # Full paths to the model files inside File_dump
    cosine_sim_path = os.path.join(file_dump_dir, 'cosine_sim.pkl')
    df_path = os.path.join(file_dump_dir, 'df.pkl')

    # # Retrieve the cleaned dataset and saved model
    # with open(cosine_sim_path, 'rb') as f:
    #     cosine_sim = pickle.load(f)

    # with open(df_path, 'rb') as f:
    #     df = pickle.load(f)
    df = joblib.load(df_path)
    cosine_sim = joblib.load(cosine_sim_path)    
    
    # Convert the input title to lowercase
    title = title.lower()

    # Convert all titles in the DataFrame to lowercase
    df['title_lower'] = df['title'].str.lower()

    # Use fuzzy matching to find the closest match to the user's title
    titles = df['title_lower'].tolist()

    # Find the closest match and its score
    match = process.extractOne(title, titles, score_cutoff=threshold)

    # If no match is found, return False
    if match is None:
        return False

    # Get the title of the best match
    best_match_title = match[0]

    # Create a new Series with lower case titles as index
    indices_lower = pd.Series(df.index, index=df['title_lower']).drop_duplicates()

    # Match the book with the corresponding index
    idx = indices_lower[best_match_title]

    # Get the pairwise similarity scores of all books with that book
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the books based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar books
    sim_scores = sim_scores[1:11]  # Starting from 1 because 0 would be the book itself

    # Get the book indices
    book_indices = [i[0] for i in sim_scores]

    # Remove the 'title_lower' column
    df = df.drop(columns=['title_lower'])

    # Return the top 10 most similar books
    return df.iloc[book_indices]
